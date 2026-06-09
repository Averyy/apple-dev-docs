# Getting started with script graphs

**Framework**: Reality Composer Pro

Build interactive, code-free 3D experiences using the visual node-based script graph editor.

#### Overview

The Script Graph Editor provides a code-free way to build many common RealityKit behaviors and interactions.

- Each graph is hosted by a Scripting Component either directly or as an asset, and primarily operates on an owning entity.
- Script graphs use entry points (On Initialize, On Update, On Collision, On Tap, Custom Events, and more) from which the execution flow starts and then moves or diverts through a series of connectors called Flow connections.
- The script graph Scripting component lets you declare variables that persist and update across frames.
- As with other graphs, you can create subgraphs to group and help manage your script graph as it gains complexity.
- Script graphs cannot create full UIs. They support only simple text-based layouts through a Text component. Use SwiftUI to build the UI for your app.

> 💡 **Tip**: Script graphs — as with the rest of Reality Composer Pro — are designed to build for RealityKit. You don’t need Swift experience, but familiarity with the RealityKit Entity Component System helps. For more information, see [`RealityKit`](https://developer.apple.com/documentation/RealityKit).

The following screenshot shows a simple script graph.

- The **blue connecting line** between the nodes On Update and Set Relative Transform is a Flow connection.
- The **gray connecting lines** pass data and compute values between nodes.

![A screenshot of the Script Graph showing a few nodes and simple flow.](https://docs-assets.developer.apple.com/published/eaa6868a511e01296d7a36e0ec2d8922/ScriptGraph%402x.png)

##### Review Graph Editor Basics

See [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md) to learn about general navigation and common features in the Reality Composer Pro Graph Editor.

##### Create a Basic Script Graph

1. In the Project Browser, Control-click the folder where you want your script graph, and then click **New** > **Script Graph**.
2. Enter a name for your script graph, and then press Enter.
3. Double-click your script graph to open it.
4. To add your first node, press **N** or the Space bar. You can also Control-click and then select **Add Node** to add your first node to the graph.

> 💡 **Tip**: If you know what you’re looking for, use the Search box in the Node Selector to narrow the list.

Script graphs generally start with an entry point node.

- Entry point nodes (such as On Update or On Initialize) are the only nodes with a blue Flow connector.
- Entry point nodes do not have an input.

##### Review Script Graph Node Types

The Script Graph Editor provides a wide range of nodes. The following is a broad overview of the available node types.

- **Control Flow nodes** — Flow nodes provide logic functions, such as IF/THEN, AND, and OR expressions, including functions for delaying execution.
- **Array nodes** — Nodes that let you create simple or complex arrays and get, set, and enumerate elements in them.
- **Collision nodes** — Nodes such as `OnCollisionBegin` and `OnCollisionEnded` that correspond to RealityKit events. Most events available in RealityKit have a corresponding node in the script graph.
- **Math and operational nodes** — Nodes for performing simple or complex mathematical operations.
- **Entity nodes** — Nodes that operate directly on entities, performing functions such as finding an entity by name in the hierarchy, getting entity properties, enabling or disabling an entity, checking for the existence of a component, and assigning a component.
- **Animation & Audio nodes** — Nodes for starting and stopping animations, audio playback, and similar functions.
- **Input nodes** — Nodes to handle input from keyboards, mice, gestures (tapping, dragging, and more), and ARKit.
- **Material nodes** — Nodes for changing shader materials based on interactions in a scene. For example, a script can tell a shader graph to adjust itself in response to scene interactions.

##### Add a Script Graph to an Entity

1. Select your entity.
2. In the Inspector, click **Add Component** > **Scripting**.
3. In the Inspector, click Script, and then select **Graph Script Source**.
4. Click **Edit** to open an empty script graph.

##### Preview Your Script Graph

You can preview your script graphs in action using Reality Composer Pro’s Preview on Device feature. See [`Linking an Xcode project`](realitycomposerpro-essentials-linkingxcodeproject.md) to learn how.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/getting-started-with-script-graphs)*