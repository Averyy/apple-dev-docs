# Getting started with Script Graphs

**Framework**: Reality Composer Pro

Build interactive, code-free 3D experiences using a visual, node-based editor in Reality Composer Pro.

#### Overview

The Script Graph Editor provides a code-free way to build many common RealityKit behaviors and interactions. A Scripting component hosts each graph either directly or as an asset, and the graph primarily operates on the owning entity.

Script Graphs use entry points — such as **On Initialize**, **On Update**, **On Collision**, **On Tap**, and **Custom Events** — as the starting point for execution flow. Execution then travels through a series of connectors called Flow connections. The Scripting component also lets you declare variables that persist and update across frames. As with other graphs, you can create subgraphs to group and manage your script graph as it gains complexity.

> **Note**: Script Graphs cannot create full user interfaces. They support only simple text-based layouts through a Text component. Use SwiftUI to build the user interface for your app.

#### Review Graph Editor Basics

Before working with Script Graphs, review the graph editor basics in [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md).

> 💡 **Tip**: Script Graphs, like the rest of Reality Composer Pro, target RealityKit. You don’t need Swift experience, but familiarity with the RealityKit Entity Component System helps. For more information, see [`RealityKit`](https://developer.apple.com/documentation/realitykit).

The following screenshot shows a simple Script Graph.

- **Blue (Flow) connecting lines** between the nodes On Update and Set Relative Transform carry execution flow between nodes.
- **Gray (Data) connecting lines** pass values and compute results between nodes.

![A screenshot of the Script Graph Editor showing the On Update node connected to the Set Relative Transform node. A blue line carries the execution flow between them; gray lines carry data values.](/images/RealityComposerPro/ScriptGraph@2x.png)

#### Choose How to Attach a Script Graph to an Entity

If you need to share a script across multiple entities or encapsulate it as a subgraph, create a **Prototype**. A Prototype lets you reuse the script graph in other graphs, or as a subgraph of a component-owned entity. Otherwise, attach the script directly to a **Scripting component** on the entity. For more information about Prototypes, see [`Reusing assets with prototypes and instances`](realitycomposerpro-essentials-understandingprototypes.md).

#### Create a Basic Script Graph

In the Project Browser, Control-click the folder where you want your Script Graph, then click **New** > **Script Graph**. Enter a name for your Script Graph, then press Enter. Double-click your Script Graph to open it.

To add your first node, use the methods described in [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md).

> 💡 **Tip**: If you know what you’re looking for, use the Search box in the Node Selector to narrow the list.

Script Graphs generally start with an entry point node. Entry point nodes (such as **On Update** or **On Initialize**) have a blue Flow output connector but no Flow input — they initiate execution rather than receiving it from another node.

To build a simple working graph, add an **On Update** entry point node, then add a second functional node such as **Set Relative Transform**. Drag from the blue Flow output connector on **On Update** to the blue Flow input connector on the second node. The line turns blue to confirm a valid Flow connection.

#### Review Script Graph Node Types

The Script Graph Editor provides nodes in several categories. Entry point nodes (such as **On Update** and **On Initialize**) begin the execution flow. Control flow nodes provide logic such as IF/THEN, AND, and OR expressions, and nodes that delay execution. Array nodes let you create and manipulate collections of values.

Once you have entities in your scene, entity nodes let you find entities by name, read and write entity properties, enable or disable entities, check for components, and assign components. Collision nodes such as On Collision Began and On Collision Ended correspond to RealityKit events — most RealityKit events have a matching node in the Script Graph.

Math and operational nodes handle simple or complex mathematical operations. Animation and audio nodes start and stop animations and audio playback. Input nodes handle input from keyboards, mice, gestures, and ARKit. Material nodes let a script tell a shader graph to adjust itself in response to scene interactions.

#### Add a Script Graph to an Entity

Select your entity, then in the Inspector click **Add Component** > **Scripting**. Click **Script** and select **Graph Script Source**. Click **Edit** to open an empty Script Graph.

#### Preview Your Script Graph

You can preview your Script Graphs in action using the Simulate feature in Reality Composer Pro. Click **Simulate** in the toolbar to run the scene — entry points such as **On Initialize** fire immediately and **On Update** runs each frame. Use the simulation to confirm your Script Graph executes as expected before deploying to a device.

For more information about previewing and running simulations, see [`Previewing content and running simulations`](realitycomposerpro-essentials-previewcontentrunsimulations.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/getting-started-with-script-graphs)*