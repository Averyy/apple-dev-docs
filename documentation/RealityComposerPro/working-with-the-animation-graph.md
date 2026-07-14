# Working with the Animation Graph

**Framework**: Reality Composer Pro

Build character animation state machines visually using the Animation Graph in Reality Composer Pro.

#### Overview

Use animation graphs to create custom animations in a visual, node-based, code-free workflow. Using the Animation Graph, you can create tags and conditions to control the flow between different animation states. For general Graph Editor navigation and features, see [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md).

![Screenshot of animation graph](https://docs-assets.developer.apple.com/published/02e03d4d0cfb29d97c07839d0be1bf0f/AnimationGraph%402x.png)

#### Create an Animation Graph

In the Project Browser, Control-click a folder and choose **New** > **Animation Graph**. Enter a name for the animation graph, then double-click it to open it in the Animation Graph Editor.

In the Inspector, click **Skeleton Definition** to select the skeleton definition you want to use. For imported entities, Reality Composer Pro creates the skeleton definition when you import the entity — including all dependencies such as blend masks and inverse kinematic rigs. Then select a **Preview Entity** to control which entity appears in the preview window. Change this option to preview your animations for different entities that share the same skeleton definition.

#### Add Animation Graph Inputs

Inputs provide a variety of parameters that can control the animation that plays at runtime. For example, an Input parameter named Jump can trigger a jumping animation.

#### Add an Input

In the Inspector, under **Inputs**, click **[+]** to add an input. Choose an **Input Parameter** type:

- Bool Parameter
- Float Parameter
- Int Parameter
- Option Parameter
- Rotation Parameter
- Trigger Parameter
- Vector Parameter

Click the name field to update the parameter name if needed, then set the **Default Value** and toggle **Read Only** as appropriate.

![Screenshot of adding an input modal](https://docs-assets.developer.apple.com/published/8523c70ed70d87d6d624a01f24f25e07/AddInput%402x.png)

#### Add and Configure a State Machine Node

A State Machine node defines the states your animation can occupy and the conditions that trigger transitions between them.

In your animation graph, press N (or spacebar) and select the **State Machine** node. Double-click it to open the empty space inside the node where you can add states and conduits.

Control-click anywhere in the empty space and choose **Add State**. In the Inspector, click the **Name** field and give your state a name. Enable any applicable toggles for your state: **Start State**, **End State**, or **Pass Through**.

To add a tag to the state, click **[+]** next to **Tags**, click the Tag field and select a tag, then click the field next to the tag and choose when to activate it:

- **On Enter** — The state machine activates the tag when the entity enters the specified state.
- **On Exit** — The state machine activates the tag when the entity exits the specified state.
- **On Enter and Exit** — The state machine activates the tag when the entity enters the state and when the entity exits the state.
- **While Active** — The state machine keeps the tag active as long as the entity remains in the specified state.

![Screenshot of the State Machine editor showing tag activation options (On Enter, On Exit, On Enter and Exit, While Active)](https://docs-assets.developer.apple.com/published/07cac85823be9dbadd0f96202e23b157/Conditions%402x.png)

> 💡 **Tip**: When editing a State Machine, click a State to view or change its associated tags and properties.

#### Use Animation Graph Tags

Attach tags to animation states using a State Machine node, then use those tags as conditions to trigger state transitions. For example, while an entity is in a state called `CarryingHeavyObject`, the state machine tags the current state with `HeavilyEncumbered`. When the `HeavilyEncumbered` tag is active, you can trigger a different animation state.

Tags activate using the same options described in the State Machine section above: On Enter, On Exit, On Enter and Exit, and While Active.

#### Add an Animation Graph Tag

In the Inspector panel, under **Tags**, click **[+]** to add a tag. Choose the **Type**: Internal, Play Audio, or Enable/Disable Entity. Click the name field to enter a name for the tag.

![Screenshot of the Inspector panel showing the Add Tag section with Internal, Play Audio, and Enable/Disable Entity tag type options](https://docs-assets.developer.apple.com/published/34cd56134bf0e32faef4e07d62620b65/AddTag%402x.png)

#### Edit or Delete Animation Graph Tags

To edit a tag, click it and then edit its properties in the Inspector. To delete a tag, click to select it and then click **[-]**.

#### Connect Conduits Between States

A conduit is a transition state that lets you route multiple states through a shared condition, so you define the condition once rather than repeating it on each state-to-state transition. A conduit can also branch to multiple different destination states.

Click the edge of a state and drag the arrow to another state.

#### Add a Condition to a Conduit

Control-click anywhere in the empty space and choose **Add Conduit**, then drag an arrow from the edge of the conduit to a State.

Control-click the conduit connector, choose **Add Condition**, and select a condition type (Bool, Finished, Float, and so on).

![Screenshot of the context menu for adding a condition to a conduit](https://docs-assets.developer.apple.com/published/f3a3b52a4fa8532b5f678cb9b88c34bc/Transitions%402x.png)

In the Inspector, under **Conditions**, configure your condition. Click the operator icon to change the comparison operator (==, !=, and so on). Click **Settings** to compare against a fixed value or a parameter.

![Screenshot of the condition editor panel showing a configured condition with operator settings](https://docs-assets.developer.apple.com/published/45bdd5cbb570a189ce3a0390c90be7ca/AddCondition%402x.png)

> 💡 **Tip**: The editor displays different conditions in different colors — for example, trigger conditions appear as blue, while boolean conditions appear as green.

#### Preview Your Animation

In the Animation Graph, at the top of the screen, click **Debug Graph** and then click **Play**.

Preview how your animations appear and watch the visual flow between nodes — indicated by animated connectors in the Animation Graph — as the entity enters and exits states. In the Inspector panel **Tags** section, watch tags activate and deactivate — indicated by pulsing dots next to the tag names — as your animation plays.

![Screenshot activating the debug menu](https://docs-assets.developer.apple.com/published/0b9794b972b7a6897b6098b43cd69ab7/DebugGraph%402x.png)

#### Apply an Animation Graph to an Entity

In the Scene Hierarchy, click an entity. In the Inspector, click **Add Component** and choose **Animation Graph**. Click the **Animation Graph** field and select the animation graph you want to apply from the pop-up menu.

![Screenshot of the animation graph component](https://docs-assets.developer.apple.com/published/dc356a2e7374bcc76c9db96fbf90513c/AnimGraphComponent%402x.png)

#### Animation Graph Nodes

The Animation Graph Editor provides a range of nodes organized by category. Each node performs a specific operation on poses, skeletons, or animation data.

- Blend nodes - **Add** — Adds two poses.
- **Blend 1D** — Blends a number of samples from child nodes distributed along a single axis.
- **Blend Mask** — Filters a pose by applying per-joint weights from a blend mask.
- **Subtract** — Subtracts one pose from another.
- Control flow nodes - **State Machine** — Evaluates a state machine.
- Inverse Kinematics (IK) nodes - **Constraint Parameters** — Parameters for a single named rig constraint.
- **Foot Placement** — Adjusts foot positions on terrain using inverse kinematics and constraints.
- **Full Body IK Node** — Full body inverse kinematics solver node with output pose based on the child pose and rig-defined constraints.
- **Joint Parameters** — Parameters for a single named rig joint.
- Modifier nodes - **Motion Warping** — Adjusts animation playback speed to ensure root motion reaches a target position.
- **Root Motion Generation** — Moves the root joint to the desired position and orientation over time.
- Output nodes - **Final Pose** — The final pose of the animation.
- Source nodes - **Animation Clip** — Represents an animation clip at edit time. Plays an animation resource using keyframes.
- **Bind Pose** — Returns the bind pose of the current skeleton.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-animation-graph)*