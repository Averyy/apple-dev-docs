# Building an advanced Animation Graph

**Framework**: Reality Composer Pro

Drive a character’s locomotion state machine from a Script Graph at runtime.

#### Overview

An Animation Graph is a visual, node-based description of how a character animates: which clips play, how they blend together, and when the character switches from one motion to another. Instead of hand-coding transition logic, you connect nodes from a handful of categories — Source nodes that supply raw animation clips, a Control Flow node called a State Machine that branches between named states, Modifier nodes that blend or reshape poses, and a single Output node that hands the final pose to the entity’s skeleton. The graph evaluates this network continuously and drives whichever entity you assign it to.

For the fundamentals of building an Animation Graph — node categories, State Machines, Tags, and Transition Conditions — see [`Working with the Animation Graph`](working-with-the-animation-graph.md).

![Screenshot of an Animation Graph in Reality Composer Pro.](https://docs-assets.developer.apple.com/published/e80f5c10efe80278499296ab67168cf9/AnimationGraph3%402x.png)

Two features extend a graph beyond its own boundaries. Tags let a state machine’s states announce their playback status. States can be entering, looping, or exiting, so both the graph itself and outside systems can react. Inputs expose graph parameters, such as a speed value or a jump trigger, that something outside the graph can set. That “outside” system is typically a [`Getting started with Script Graphs`](getting-started-with-script-graphs.md), Reality Composer Pro’s event-driven runtime scripting surface: it reacts to gameplay events like a collision, then reads a Tag or drives an Input to change what the character’s Animation Graph does next.

This article builds a small locomotion graph — an Idle, Walk, and Run state machine blended by speed — assigns it to a character, previews it from three different surfaces in the editor, and wires a Script Graph that reads and drives its state. It also covers [`AnimationGraphComponent`](https://developer.apple.com/documentation/RealityKit/AnimationGraphComponent), the public RealityKit struct that attaches the compiled graph to an entity and exposes its runtime state to Swift.

#### Create an Animation Graph

Create the asset from the Project Browser by clicking **[+]**  > **Animation** > **Animation Graph**, then give it a descriptive name, such as “CharacterLocomotion.” Opening the asset switches Reality Composer Pro to the Animation Workspace, a layout pre-configured for authoring Animation Graph assets, with the graph canvas as the central surface.

Before adding nodes, set the graph’s asset-level Skeleton Definition to the skeleton the graph drives — every Animation Clip and pose node you add later resolves its joints against this skeleton, so set it first. If your project already has retargeted animation clips in an animation library that references the same Skeleton Definition, you can drop those clips directly into the graph as Source nodes without any additional setup.

#### Add Animation Sources

Every Animation Graph node belongs to one of five categories: Source, Control Flow, Modifier, Inverse Kinematics, and Output. Open the Node Insertion Menu with N or the Space key to browse them.

Add two Animation Clip nodes from the Source category and point them at your character’s Walk and Run clips. On their own, these nodes only output a single clip’s pose.

![Screenshot of a Reality Composer Pro Animation Graph with Walk, Run, and Idle nodes connected to a State Machine node.](https://docs-assets.developer.apple.com/published/59bfd4acfa96a4795fc6a641a6f12896/AnimationGraph6%402x.png)

#### Blend Sources By Speed

To blend between the Walk and Run clips based on speed, add a Blend 1D node from the Modifier category and connect both clip outputs into it. Blend 1D opens an embedded Blend Space view, a small grid editor where you arrange animation samples along a single parameter axis. Place the Walk sample near the low end of the axis and the Run sample near the high end; the node needs at least two samples to blend anything, and you can add, remove, rename, or reposition samples at any time.

![Screenshot of Reality Composer Pro Animation Graph nodes and the Blend definition parameters shown in the Inspector.](https://docs-assets.developer.apple.com/published/322296528c5bde64fc810e734ee8776c/AnimationGraphNodes%402x.png)

To drive that axis at runtime rather than hardcoding a value, add a graph-level Input of type Float named “Speed,” then connect it to the Blend 1D node’s blend parameter. As the Speed input rises from 0 to its maximum, the node crossfades smoothly from the Walk sample to the Run sample.

> **Note**: Animation Graph nodes pass pose data along typed pins, not execution order. There’s no concept of an execution-flow or event pin here — that vocabulary belongs to Script Graph, which you’ll meet later in this article.

#### Branch States with a State Machine

A Blend 1D node handles blending within a single locomotion pose, but a character also needs to switch between distinct behaviors — standing still versus moving. Add a State Machine node from the Control Flow category to handle that branching. Inside it, create three States: Idle, Walk, and Run, and rename each one to match. Idle sources a standing-still Animation Clip directly; Walk and Run can both route through the Blend 1D node you built in the previous section, since that node already blends between exactly those two clips.

![Screenshot of the Reality Composer Pro Animation State Machine Node.](https://docs-assets.developer.apple.com/published/2a703d622b1e05d7db9855c200957750/AnimationGraphStateMachine%402x.png)

Connect Idle to Walk, and Walk to Run, with Transitions — connect Conduits between them if you want to share transition conditions across more than one pair of states. Each Transition carries one or more Transition Conditions; Animation Graph supports several condition types, but this graph only needs Float. Give the Idle-to-Walk transition a Float condition that fires once the Speed input crosses a small threshold above zero, and give Walk-to-Run a higher threshold on the same input, so the character’s state advances in step with the same value driving the blend.

With the state machine wired, connect its output to a Final Pose node from the Output category. Final Pose is where every graph in this article ultimately terminates — it’s the node that hands the resolved pose to the entity’s skeleton for rendering.

#### Expose Graph State with Tags

A state machine’s states can carry Tags, which announce when a state reaches a particular point in its playback lifecycle. Select the Run state and add an Internal Tag named “IsSprinting,” then set its logic mode to OnEnter so the tag reports active as soon as the character enters the Run state. Other logic modes are available for detecting a state’s full duration, its exit moment, or each loop iteration; this graph only needs to know the instant Run begins, so OnEnter is the right choice here.

![Screenshot of Reality Composer Pro Animation State Node expanded with State Tags shown in the Inspector.](https://docs-assets.developer.apple.com/published/cd7c08eb123c77fca63ee5590bf8fb21/AnimationGraphStateTags%402x.png)

Every tag placed anywhere in the graph also appears in the graph-level Tags panel, listing each tag’s Name, Type, and current Status. You can check a tag two ways: from inside the state machine, using a Tag-type Transition Condition to branch on whether another state’s tag is active, or from outside the graph entirely, by reading the tag’s status from Swift or a Script Graph. That second path is the hook this article uses later to bridge into Script Graph and Swift — keep it distinct from Script Graph’s own Events, which is a different mechanism in a different graph type; the Drive the graph from a Script Graph section covers it separately.

#### Assign the Graph to a Character Entity

With the graph built, select the character entity in the Hierarchy Tab, open the Inspector, and choose Add Component > Animation Graph. Bind the CharacterLocomotion asset you created earlier to this component. Reality Composer Pro lists Animation Graph under the Animation heading alongside Animation Library and Skeleton Debug, describing it as the component that scripts an entity’s animation behavior through a graph interface.

Confirm the component’s bound graph shares the same Skeleton Definition as the character’s rig — a mismatch here is the most common reason a correctly wired graph produces no visible motion, since the graph’s Animation Clip and pose nodes resolve joints against whichever skeleton the graph itself declares.

#### Preview the Graph in the Editor

Reality Composer Pro gives you three separate surfaces for checking this graph’s behavior. Each answers a different question. The Animation Graph editor’s own Preview Viewport, built directly into the graph’s Interface Layout, gives you real-time feedback as you edit nodes — useful while you’re still wiring the Blend 1D node or adjusting a transition threshold. The shared Preview Tab, common to every asset type in Reality Composer Pro, shows the selected graph updating live against its own Camera and Lighting environment settings. Use it to check the character’s appearance independent of the graph editor itself.

The Simulate Tab goes a step further by letting you play the graph over time rather than viewing a static snapshot: use Play, Pause, and Restart alongside a Playback Speed control ranging from 1/10x to 10x, plus the same shared camera, lighting, and debug-view controls found elsewhere. Scrub the Speed input up and down here to confirm the Walk-to-Run blend and the state machine’s transitions behave the way you expect before moving on to gameplay integration.

#### Drive the Graph From a Script Graph

Everything up to this point lives entirely inside the Animation Graph editor. Getting a Trigger input or a Tag to respond to gameplay — a collision, a button press — requires a second, separate graph type: Script Graph, Reality Composer Pro’s event-driven visual scripting surface for runtime logic. Authoring a Script Graph produces a `ScriptingComponent` — the editor and its JavaScript-facing API call it `ReScriptingComponent` — that you attach to an entity alongside its Animation Graph component.

Reality Composer Pro links `RealityKitScripting` automatically; a plain RealityKit app project needs it linked manually so its `ScriptingSystem` can execute `ScriptingComponent` instances at runtime.

A Script Graph typically begins with a node from its Events category — reacting to a Collision event or an Input event, for example — and then reaches into the character entity’s components to read or change state. The Component category supplies that bridge. Get Component retrieves the entity’s Animation Graph component. Set Component writes changes back to it. Has Component checks whether the component exists before you try to use it.

![Screenshot of the Animation Graph Get Component Node with AnimationGraph specified for the Component Type.](https://docs-assets.developer.apple.com/published/d9dcfa90c476258caaa8c01d45a241ac/AnimationGraphGetComponent%402x.png)

For this locomotion graph, wire a Script Graph that starts from a Collision event, uses Get Component to reach the entity’s Animation Graph component, and then either reads whether the “IsSprinting” Tag is currently active or sets the “Jump” Trigger input you’d expose alongside Speed, depending on what the collision represents.

#### Observe Graph State From Swift

RealityKit exposes the compiled graph’s runtime state to Swift through [`AnimationGraphComponent`](https://developer.apple.com/documentation/RealityKit/AnimationGraphComponent), the same component the Add Component menu and Script Graph’s Get Component node work with. Attach it with [`init(graph:)`](https://developer.apple.com/documentation/RealityKit/AnimationGraphComponent/init(graph:)), or read it back from an entity that already has one:

```swift
if let animationGraph = character.components[AnimationGraphComponent.self] {
    let isSprinting = animationGraph.activeTags.contains { $0.name == "IsSprinting" }
    if isSprinting {
        logger.info("Character is sprinting")
    }
}
```

[`activeTags`](https://developer.apple.com/documentation/RealityKit/AnimationGraphComponent/activeTags) reports every Tag that fires or is active during the graph’s most recent evaluation tick — including the “IsSprinting” Tag from earlier — and [`activeStateMachineNodes`](https://developer.apple.com/documentation/RealityKit/AnimationGraphComponent/activeStateMachineNodes) reports each State Machine node’s current and previous state IDs for debugging. Both are read-only views onto the graph’s last tick; changing what a character animates still requires editing the graph itself or driving its Inputs and Tags from the editor or a Script Graph.

If your app also plays animation clips directly, independent of an Animation Graph, RealityKit provides a separate, simpler surface for that:

- [`AnimationLibraryComponent`](https://developer.apple.com/documentation/RealityKit/AnimationLibraryComponent) holds an entity’s named animation resources
- [`playAnimation(_:transitionDuration:startsPaused:)`](https://developer.apple.com/documentation/RealityKit/Entity/playAnimation(_:transitionDuration:startsPaused:)) plays one and returns an [`AnimationPlaybackController`](https://developer.apple.com/documentation/RealityKit/AnimationPlaybackController) for playback control
- [`AnimationEvents`](https://developer.apple.com/documentation/RealityKit/AnimationEvents) reports playback notifications through Combine
- [`BindTarget`](https://developer.apple.com/documentation/RealityKit/BindTarget) identifies a specific animatable property such as [`BindTarget.jointTransforms`](https://developer.apple.com/documentation/RealityKit/BindTarget/jointTransforms) or [`BindTarget.parameter(_:)`](https://developer.apple.com/documentation/RealityKit/BindTarget/parameter(_:)). These APIs act on individual animation clips. RealityKit’s documentation doesn’t specify how they behave if you combine them with an Animation Graph’s state machine, Tags, or Inputs on the same entity, so test that combination before relying on it.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Building multi-track animation sequences](building-multi-track-animation-sequences.md)
  Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.
- [Automating motion path creation with editor-scripting commands](automating-motion-path-creation-with-editor-scripting-commands.md)
  Build the same multi-track Sequence and Motion Path shown in the Sequencer UI programmatically, by chaining editor-scripting commands together.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-an-advanced-animation-graph)*