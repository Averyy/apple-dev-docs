# Working with the Graph Editor

**Framework**: Reality Composer Pro

Use Reality Composer Pro’s node-based editor to build materials, animations, audio effects, and scripts without writing code.

#### Overview

Reality Composer Pro’s **Graph Editor** is a node-based, no-code editor you can use to create a variety of assets, including materials, animations, audio effects, and scripts.

Reality Composer Pro tailors each type of Graph Editor — Script Graph, Shader Graph, and Animation Graph — to the specific asset it creates. Each shares a common set of controls covered in this article.

For example, a Script Graph uses different nodes and options than a Shader Graph. The following screenshots compare the two:

![A screenshot of a Shader Material Graph in the Reality Composer Pro Graph Editor.](https://docs-assets.developer.apple.com/published/b2574806a6f2e316b464429b6c7d2708/ShaderGraph%402x.png)

![A screenshot of a Script Graph in the Reality Composer Pro Graph Editor.](https://docs-assets.developer.apple.com/published/eaa6868a511e01296d7a36e0ec2d8922/ScriptGraph%402x.png)

#### Open the Graph Editor

You can open the Graph Editor in two ways. To open a graph file directly, double-click a graph file in the project browser — such as a Shader Graph Material or Script Graph — to open it in the respective graph editor.

To open a graph file from a new tab, from the main menu choose **Tab** > **New Tab** to open a blank graph tab in your workspace. Then drag a graph file — such as a Script Graph, Shader Graph Material, or Animation Graph — from the project browser into the Graph tab.

![A screenshot showing how to open a graph file in the Reality Composer Pro Graph Editor from a new tab.](https://docs-assets.developer.apple.com/published/1afd0c323a69654550fb0477279b5aa1/GraphEditor-NewTab%402x.png)

#### Navigate the Graph Editor Workspace

As your graphs grow more complex, these controls help you view, organize, and navigate the workspace.

Use the mouse scroll wheel to zoom in and out.

Use the search bar above the graph to search for a specific node — the node centers in the graph.

Control-click in the Graph workspace (or choose **Editor** in the main menu) to access these workspace-wide layout options:

- **Clean up** — Reality Composer Pro organizes the on-screen nodes for better visibility.
- **Zoom Fit** — Reality Composer Pro zooms and centers the graph in the workspace window.

With one or more nodes selected, you can also apply these layout operations to just the selected nodes:

- **Align** — Aligns the selected nodes left, right, top, or bottom. Requires more than one node to be selected.
- **Distribute** — Distributes and spaces the selected nodes equally, either horizontally or vertically.

#### Add Nodes to a Graph

The Graph Editor offers three ways to add a node.

Press **N** or the space bar, then choose a node from the node selector.

Alternatively, Control-click anywhere in the Graph workspace, click **Add Node**, and then choose a node from the selector.

You can also click and drag a node’s input or output connector and release in any empty space in the Graph Editor — releasing in an empty space opens a context-sensitive node selector that shows only nodes compatible with what you’re connecting.

> 💡 **Tip**: You can click the name of any node in a graph to rename it to something more descriptive of its function — for example, Wait at Door, Pick Up Key, or Open Door A.

![A screenshot showing how to rename a node in the Reality Composer Pro Graph Editor by clicking its name.](https://docs-assets.developer.apple.com/published/795605d91c69f404783c0be415e6eed9/Rename%402x.png)

#### Connect Input Output and Subgraph Nodes

To connect two nodes, drag from an output port on one node to a compatible input port on another. The Graph Editor prevents you from attaching a connector to an incompatible port and highlights valid connections as you drag.

When you create an **Input**, **Output**, or **Subgraph** node, notice that they all have a **+** connector. When you drag a connection from the **+**, the Graph Editor determines the name and type of the new input or output automatically based on the connection.

![A screenshot of Input, Output, and Subgraph nodes in the Reality Composer Pro Graph Editor, each showing a + connector.](https://docs-assets.developer.apple.com/published/e189d3a25753eb6a1d3a469bbcfb4be6/InputOutputSubgraph%402x.png)

The graph type determines whether you can create additional inputs and outputs. For example, a Shader Graph doesn’t allow you to create additional outputs.

#### Create a Subgraph

You can select a collection of nodes and turn them into a Subgraph to help organize a large, complex graph. You can also convert Subgraphs into reusable prototypes to share across other graphs.

To create a Subgraph, Control-click a single node and then click **Compose Subgraph**. Or, drag to select multiple nodes, Control-click the selected nodes, and then click **Compose Subgraph**.

To expand a subgraph back into the parent graph, Control-click the subgraph node and click **Decompose Subgraph**. Reality Composer Pro moves the internal nodes and connections into the parent graph, rewires external connections directly to the surrounding graph, and then removes the subgraph node itself.

> **Note**: For information about prototypes and Prototype Subgraph commands (Convert to Prototype Subgraph, Open Subgraph Prototype, Open Subgraph Instance, and Remove Node Override), see [`Reusing assets with prototypes and instances`](realitycomposerpro-essentials-understandingprototypes.md).

#### Add Comments to Graphs

Use comments to help organize, describe, and annotate complex graphs and subgraphs. To add a comment to a single node, Control-click the node and choose **Add Comment Box**. To add a comment to multiple nodes, click and drag a selection box around the nodes and press **C** on the keyboard. Alternatively, Control-click any of the selected nodes and choose **Add Comment Box**.

![A screenshot showing a comment box added around multiple selected nodes in the Reality Composer Pro Graph Editor.](https://docs-assets.developer.apple.com/published/6595af9f5eb6de95ff844f03e8e98218/CommentBox%402x.png)

#### Edit Copy or Color Code Comments

These commands apply to comment boxes. Control-click any comment to open its context menu, and then do any of the following:

- **Cut**, **Copy**, or **Paste** — Cut, copy, or paste a comment and its associated nodes.
- **Delete** — Deletes the comment only. Deleting a comment doesn’t delete the nodes associated with it.
- **Duplicate** — Makes a duplicate of the comment and its contents (nodes). The duplicate includes the nodes from the original comment, but none of the nodes have connections.
- **Change Color** — Opens a color selector where you can change the color, opacity, and other visual characteristics for the comment. To access it, click the ellipsis (three dots) in the context menu.

#### Use Clipboard Commands to Copy Paste or Delete Nodes

These commands apply to selected nodes. With one or more nodes selected, Control-click and then use any of the following commands:

- **Cut** — Cuts the selected nodes.
- **Copy** — Copies the selected nodes.
- **Duplicate** — Duplicates the selected nodes.
- **Delete** — Deletes the selected nodes.

![A screenshot of the complete graph node context menu in the Reality Composer Pro Graph Editor, showing all available options.](https://docs-assets.developer.apple.com/published/780608881870365d9518f80c3ef2f41a/NodeContextMenu%402x.png)

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Explore the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Edit a prototype once and propagate the change to every placement of that asset in a scene.
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-grapheditoroverview)*