# Defining a behavior with Behavior Trees

**Framework**: Reality Composer Pro

Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.

#### Overview

A Behavior Tree is a construct that defines a prioritized hierarchy of behavior used by an entity in a scene. For example, use a Behavior Tree to control which path a duck takes across a pond.

Similar to other graphs, a Behavior Tree consists of different nodes specifically created for defining an in-game entity’s behavior and decision making. Each type of node either manages the entity’s overall traversal through the tree or provides it with some type of ability.

When a Behavior Tree has completed processing — meaning the tree has traversed the last leaf node — it resets to the Root (beginning) node, although you can modify this behavior.

![A Behavior Tree in the Reality Composer Pro editor showing a Root node connected to Selector and Sequence composite nodes, with Action nodes as leaves.](/images/RealityComposerPro/BehaviorTree@2x.png)

#### Combine Behavior Trees with a Decision Making Layer

While Behavior Trees define how an entity behaves, by themselves they do not contain complete logic for autonomous decision making. The decision-making logic for the entity typically comes from an external source:

- Swift application code
- Visual scripting (a Script Graph) in Reality Composer Pro
- A developer-created state machine solution
- An LLM that selects which behaviors to run

No matter how you choose to drive decision making in your app, you drive the Behavior Tree by setting the parameter values its nodes understand.

- The decision-making logic decides what type of behavior the entity performs.
- The Behavior Tree defines the actual steps necessary to perform the behavior.

#### Create a Behavior Tree

Before you begin, see [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md) for an overview of navigating the Graph Editor.

In the Project Browser, click **[+]** and then click **Animation** > **Behavior Tree**. You can also Control-click inside a folder and then click **New** > **Animation** > **Behavior Tree**. Double-click your behavior tree to open it in the Behavior Tree editor.

#### Apply a Behavior Tree to an Entity

Select an entity in the Project Browser. In the Inspector, click **Add Component** > **Behavior Tree**. Under **Behavior Tree Component**, click **[+]** to select a Behavior Tree. In the Inspector, in the Behavior Tree component:

- Under **Behavior Trees**, assign one or more available behavior trees.
- Next to **Default Tree**, select a default behavior tree for the entity.

#### Choose the Right Node Type for Your Behavior

A Behavior Tree consists of interconnected nodes that provide various types of functionality. Nodes perform behaviors and guide how the tree is traversed. Each node type, when traversed, returns a status of success (`true`), failure (`false`), or running — indicating the node is still executing and the tree should wait before advancing. Other nodes use a node’s **Return Value** to determine how tree traversal continues.

Each node has a set of specific properties you can define, which appear in the Inspector when you select the node. In addition, all node types have modifiers that let you:

- **Apply a precondition when entering the node**. If the precondition fails, the tree skips the node.
- **Loop the node**. You can optionally loop a node a fixed number of times, or until a condition is met.
- **Modify the status of the node when it returns**. You can opt to always set the status to success or failure. You can also opt to invert the status (that is, change success to failure or failure to success).

Behavior Tree nodes fall into three categories — **Root**, **Action**, and **Composite**. The **Root** node is the first default node that appears when you create a new Behavior Tree and defines the starting point for traversal. There can be only one Root node.

#### Use Action Nodes to Drive Entity Behaviors

Action nodes directly affect the entity or the scene — they perform the behaviors your Behavior Tree is designed to control. When an Action node executes, it returns success or failure based on whether the action completed. The available Action nodes are:

- **Action** — Sends entity action events on entering, updating, or returning. You can create custom actions in Swift with different event handlers.
- **Debug** — Adds custom text to the **Console** log output.
- **Move on Navigation Mesh** — Moves the entity to the specified position by navigating along a specified navigation mesh, routing around obstacles in the mesh.
- **Move To** — Moves the entity in a straight line to the specified position. You can specify the direction and the speed at which an entity travels.
- **NoOp** — Performs no operation other than its modifier processing.
- **Parameter Setter** — A flexible node that assigns values to given parameters, which can then be passed to other graphs, such as an Animation Graph. Use this to pass values to trigger an animation or perform other actions, such as playing an audio file.
- **Rotate to Face** — Rotates an entity around its y-axis to face the desired position.
- **Set Tree** — Exits the current Behavior Tree and begins processing a new tree. Use this node to create collections of Behavior Trees — each controlling different behaviors — and interconnect them for an entity.
- **Wait** — Pauses the Behavior Tree for a specified amount of time or until a condition is met, with the option to randomize wait times.

#### Control Tree Traversal with Composite Nodes

Composite nodes control how the Behavior Tree traverses its children. Each composite node type uses a different strategy to determine which child to visit next and when to stop. The three composite node types are:

- **Parallel** - Processes all children concurrently — unlike the Selector and Sequence nodes, which process their child nodes one at a time, in sequence.
- Good for having an entity perform multiple, simultaneous actions, such as turning and moving in a direction at the same time.
- All subtrees are allowed to update in the same frame.
- Success or failure of the parallel node is determined based on user-defined options: - Node is successful after **one** child succeeds.
- Node is successful after *n* children succeed (that is, success requires *n* children to succeed first).
- There is also a Success Percentage field you can define which determines the least x% of the children that must succeed in order for the parallel node to succeed.
- Upon node success, the node interrupts and stops currently running children immediately.
- **Selector** - Think of the Selector as a logical OR statement for its child nodes.
- The Selector processes children left to right. If a child fails (returns `false`), the Selector moves to the next child. It continues until it reaches the first child that returns `true`.
- After the Selector returns `true` (after encountering the first child that returns `true`), the Selector is finished and the Behavior Tree advances.
- A Selector only returns `false` if all children fail.
- Selector nodes can randomize their children. Instead of visiting children in the order you arranged them, at runtime the tree randomizes its children each time it enters the Selector node, then visits them left-to-right with the new ordering.
- **Sequence** - Sequence nodes can have one or more children.
- Child nodes are processed in a left-to-right order. As long as every node returns `true`, the Sequence continues.
- Think of a Sequence node as a type of AND operation for all child nodes. As soon as a child fails (returns `false`), the Sequence exits and the Behavior Tree advances.
- Sequence nodes can also randomize their children, like Selector nodes.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Building multi-track animation sequences](building-multi-track-animation-sequences.md)
  Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building an advanced Animation Graph](building-an-advanced-animation-graph.md)
  Drive a character’s locomotion state machine from a Script Graph at runtime.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/defining-a-behavior-with-behavior-trees)*