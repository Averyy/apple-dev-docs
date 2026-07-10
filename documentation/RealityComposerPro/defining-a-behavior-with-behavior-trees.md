# Defining a behavior with Behavior Trees

**Framework**: Reality Composer Pro

Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.

#### Overview

A Behavior Tree is a construct that defines a prioritized hierarchy of behavior used by an entity in a scene. For example, use a Behavior Tree to control which path a duck takes across a pond.

Similar to other graphs, a Behavior Tree is composed of different nodes specifically created for defining an in-game entity’s behavior and decision making. Each type of node either manages the entity’s overall traversal through the tree or provides it with some type of ability.

When a Behavior Tree has completed processing, meaning that the last leaf node has been completed, the tree resets to the Root (beginning) node, although you can modify this behavior.

![A screenshot of the Behavior Tree.](https://docs-assets.developer.apple.com/published/f887394df63c1b189c28329acdcdc8fe/BehaviorTree%402x.png)

##### Understand the Decision Making Layer

While Behavior Trees define how an entity behaves, by themselves they do not contain complete logic for autonomous decision making. The decision-making logic for the entity typically comes from another solution, such as:

- Swift application code
- Visual scripting (a Script Graph) in Reality Composer Pro
- A developer-created state machine solution
- An LLM that selects which behaviors to execute

The key is that no matter how you choose to drive decision making in your app, you communicate your wishes to the behavior tree by setting parameter values that the behavior tree nodes understand.

- The decision-making logic decides what type of behavior the entity performs.
- The Behavior Tree defines the actual steps necessary to perform the behavior.

##### Before You Begin

For an overview of navigating and working in the Graph Editor, see [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md).

##### Create a Behavior Tree

**Method 1**

1. From the Project Browser, click **(+)** and then click **Behavior Tree**.
2. Double-click your behavior tree to open it in the Behavior Tree editor.

**Method 2**

1. In the Project Browser, control-click in a folder, and then click **New** > **Behavior Tree**.
2. Double-click your behavior tree to open it in the Behavior Tree editor.

##### Apply a Behavior Tree to an Entity

1. Select an entity in the project browser.
2. In the Inspector, click **Add Component** > **Behavior Tree**.
3. In the Inspector, under **Behavior Tree Component**, click **[+]** to select a Behavior Tree.
4. In the inspector, in the Behavior Tree component: 1. Under **Behavior Trees,** assign one or more available behavior trees.
2. Next to **Default Tree**, select a default behavior tree for the entity.

##### Behavior Tree Nodes

A behavior tree comprises interconnected nodes, which provide various types of functionality. Nodes are used to perform behaviors as well as guide how the tree itself is traversed. Each node type, when traversed, returns a boolean value of `true` (the node’s processing was successful) or `false` (failed). Other nodes use a node’s **Return Value** to determine how tree traversal continues.

Each node has a set of specific properties you can define for that node, which are displayed in the Inspector when the node is selected. In addition, all node types have modifiers that let you:

- **Apply a pre-condition when entering the node**. If the precondition fails, the tree skips the node.
- **Loop the node**. You can optionally loop a node a fixed number of times, or until a condition is met.
- **Modify the status of the node when it returns**. You can opt to always set the status to success or failure. You can also opt to invert the status (that is, change success to failure or failure to success).

Behavior Tree nodes are divided into three categories — Root, Action, and Composite — each described below.

- Root nodes - **Root** — The first default node that appears when you create a new Behavior Tree. Defines the root of the tree. There can be only one Root node.
- Action nodes - **Action** — Sends entity action events on entering, updating, or returning. Allows you to create custom actions in Swift with different event handlers.
- **Debug** — Allows you to add customized text that shows up in the logging displayed in the Console.
- **Move on Navigation Mesh** — Moves the entity in a straight line to the specified position along a specified navigation mesh.
- **Move To** — Moves the entity in a straight line to the specified position. You can specify the direction and the speed at which an entity travels.
- **NoOp** — Performs no operation other than its modifier processing.
- **Parameter Setter** — A flexible node that assigns values to given parameters, which can then be passed to other graphs, such as an Animation graph. Use this to pass values to trigger an animation or perform other actions, such as playing an audio file.
- **Rotate to Face** — Rotates an entity on its z-axis to the desired position.
- **Set Tree** — Exits the current behavior tree and begins processing a new tree. Allows you to create collections of Behavior Trees, where each tree controls different behaviors, that can then be interconnected for an entity.
- **Wait** — Pauses the Behavior Tree for a specified amount of time or until a condition is met. Includes the ability to randomize wait times.
- Composite nodes - **Parallel** - Processes all children concurrently — unlike the Selector and Sequence nodes, which process their child nodes one at a time, in sequence.
- Good for having an entity perform multiple, simultaneous actions, such as turning and moving in a direction at the same time.
- All subtrees are allowed to update in the same frame.
- Success or failure of the parallel node is determined based on user-defined options: - Node is successful after **one** child succeeds.
- Node is successful after ***n*** children succeed (that is, success requires **n** children to succeed first).
- Upon node success, the node interrupts and stops currently-running children immediately.
- **Selector** - Think of the Selector as a logical OR statement for its child nodes.
- The Selector processes children left to right. If a child fails (returns False), the Selector moves to the next child. It continues until it reaches the first child that returns True.
- After the Selector returns True (after encountering the first child that returns True), the Selector is finished and the Behavior Tree advances.
- A Selector only returns False if all children fail.
- Selector nodes have the ability to randomize their children. In this case, instead of processing children left-to-right in the order that was authored, at runtime, each time the selector or sequence node is entered it will randomize its children and then visit the children left-to-right with the new ordering.
- **Sequence** - Sequence nodes can have one or more children.
- Child nodes are processed in a left-to-right order. As long as every node returns True, the Sequence continues.
- Think of a Sequence node as a type of AND operation for all child nodes. As soon as a child fails (returns False), the Sequence exits and the Behavior Tree advances.
- Sequence nodes also have the ability to randomize their children, like Selector nodes.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build and customize animation sequences to control entity movement and behavior in your scene.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Define and control character animations using a visual, node-based state machine in Reality Composer Pro.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/defining-a-behavior-with-behavior-trees)*