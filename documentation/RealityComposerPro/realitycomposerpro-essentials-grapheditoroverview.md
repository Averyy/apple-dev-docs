# Working with the Graph Editor

**Framework**: Reality Composer Pro

Add and connect nodes in Reality Composer Pro to create materials, animations, audio effects, scripts, and more.

#### Overview

Reality Composer Pro’s **Graph Editor** is a node-based, no-code editor you can use to create a variety of assets, including materials, animations, audio effects, and scripts.

The following sections cover the basics of working with the Graph Editor in general, but each type of Graph Editor (Script, Shader) is tailored to the specific asset it creates.

For example, a Script Graph uses different nodes and options than a Shader Material Graph. The following screenshots compare the two:

![A screenshot of a Shader Material Graph in the Reality Composer Pro Graph Editor.](https://docs-assets.developer.apple.com/published/b2574806a6f2e316b464429b6c7d2708/ShaderGraph%402x.png)

![A screenshot of a Script Graph in the Reality Composer Pro Graph Editor.](https://docs-assets.developer.apple.com/published/eaa6868a511e01296d7a36e0ec2d8922/ScriptGraph%402x.png)

##### Opening the Graph Editor

You can open the Graph Editor in two ways. To open a graph file directly, double-click a graph file in the project browser — such as a Shader Graph Material or Script Graph — to open it in the respective graph editor.

To open a graph file from a new tab, choose **Tab** > **New Tab** from the **Main Menu** to open a blank graph tab in your workspace, then drag a graph file — such as a Script Graph, Shader Graph Material, or Animation Graph — from the project browser into the Graph tab.

![A screenshot showing how to open a graph file in the Reality Composer Pro Graph Editor from a new tab.](https://docs-assets.developer.apple.com/published/1afd0c323a69654550fb0477279b5aa1/GraphEditor-NewTab%402x.png)

##### Adding Nodes to a Graph

The Graph Editor offers three ways to add a node. From the keyboard, press **N** or the space bar, then choose a node from the node selector. Or, control-click anywhere in the Graph workspace, click **Add Node**, and then choose a node from the selector.

You can also click and drag a connector from a node’s input or output, then release in any empty space in the Graph Editor. Releasing in empty space opens a context-sensitive node selector that shows only nodes compatible with what you’re connecting.

> 💡 **Tip**:  You can click the name of any node in a graph to rename it to something more descriptive of its function — for example, Wait at Door, Pick Up Key, or Open Door A.

![A screenshot showing how to rename a node in the Reality Composer Pro Graph Editor by clicking its name.](https://docs-assets.developer.apple.com/published/795605d91c69f404783c0be415e6eed9/Rename%402x.png)

##### Changing Node Connections

You can change connectors between nodes in the following ways:

- Click and then drag a connector to connect it to a different node. The Graph Editor prevents you from attaching a connector to an incompatible node.
- Click a connection and then press **Delete** to delete it.

> 💡 **Tip**:  A red dot displayed next to a node parameter indicates a **required parameter**. Depending on the type of parameter, this means it either requires you to enter a value or it must be connected to another node.

![A screenshot of a basic Script Graph in Reality Composer Pro, with red dots highlighting required parameters.](https://docs-assets.developer.apple.com/published/809bcc8b9abd1c7cb149caa894d02fd3/RequiredConnector%402x.png)

##### Working in the Graph Workspace

As your graphs grow more complex, use the following features to view, organize, and navigate the Graph workspace:

- Use the mouse scroll wheel to zoom in and out.
- Use the search bar above the graph to search for a specific node. The node centers in the graph.
- Control-click in the Graph workspace (or click **Editor** on the main menu) to access the following options: - **Clean up** — Reality Composer Pro organizes the on-screen nodes for better visibility.
- **Zoom Fit** — Reality Composer Pro zooms and centers the graph in the workspace window.
- **Align** — Aligns the graph Left, Right, Top, or Bottom.
- **Distribute** — Provides options to change the distribution (Horizontal or Vertical) and spacing for better readability.

##### Working with Nodes in the Graph Editor

Complex graphs can be hard to read, but the Graph Editor includes options to help you view, organize, interact with, and document them.

Control-click any node to show its context menu. The available commands fall into four groups: subgraph composition, comments, layout, and clipboard.

> 💡 **Tip**:  You can also find these options under **Editor** in the Main Menu.

**Subgraph composition.** Use these commands to create, expand, or share subgraphs:

- **Compose Subgraph** — Wraps the selected nodes (and their connections and comment boxes) into a new subgraph node placed at the selection’s center. Connections that crossed the selection boundary are rewired through auto-generated input and output nodes on the new subgraph.
- **Decompose Subgraph** — Expands a subgraph node back into the parent graph. Reality Composer Pro removes the internal nodes and connections, rewires external connections directly to the surrounding graph, and then removes the subgraph node itself.
- **Convert to Prototype Subgraph** — Promotes a local (inline) subgraph into a reusable Prototype Subgraph asset. Enter a name and location for the new prototype asset, then click **Convert**. A sheet then opens so you can choose how to handle the subgraph’s variables (copy to prototype, clear, or clear while preserving local overrides).
- **Open Subgraph Prototype** — On a prototyped-subgraph node, navigates to and opens the prototype asset that defines it (that is, the source or template). Available only when exactly one subgraph node is selected.
- **Open Subgraph Instance** — Navigates into the per-instance graph of the selected subgraph node so you can edit its instance-specific overrides. If the node is still purely inherited from its prototype, the editor creates an override first to make it editable.
- **Remove Node Override** — On an instantiated or overridden node (one whose values diverge from the prototype it inherits from), discards the local override and reverts the node to its prototype state.

**Comments.** Use this command to annotate selected nodes:

- **Add Comment Box** — Adds a comment box to one or more selected nodes to help describe or document them.

**Layout.** Use these commands to position the selected nodes:

- **Zoom Fit** — Zooms into and fits the selected nodes into the view window.
- **Align** — When more than one node is selected, aligns the nodes left, right, top, or bottom.
- **Distribute** — Distributes and spaces the selected nodes equally, either horizontally or vertically.

**Clipboard.** Use these commands to manage the selected nodes:

- **Cut** — Cuts the selected nodes.
- **Copy** — Copies the selected nodes.
- **Duplicate** — Duplicates the selected nodes.
- **Delete** — Deletes the selected nodes.

![A screenshot of the complete graph node context menu in the Reality Composer Pro Graph Editor, showing all available options.](https://docs-assets.developer.apple.com/published/780608881870365d9518f80c3ef2f41a/NodeContextMenu%402x.png)

##### Connecting Input Output and Subgraph Nodes

When you create an **Input**, **Output**, or **Subgraph** node, notice that they all have a **+** connector. When you drag a connection from the **+**, the Graph Editor determines the name and type of the new input or output automatically based on the connection.

![A screenshot of Input, Output, and Subgraph nodes in the Reality Composer Pro Graph Editor, each showing a + connector.](https://docs-assets.developer.apple.com/published/e189d3a25753eb6a1d3a469bbcfb4be6/InputOutputSubgraph%402x.png)

Depending on the type of graph, you may or may not be able to create additional inputs and outputs. For example, a Shader Graph doesn’t allow you to create additional outputs.

##### Documenting Graph Nodes

You can add comments to help describe and document nodes in your graphs.

To add a comment to a single node, control-click the node and then choose **Add Comment**.

To add a comment to multiple nodes, click and drag a selection box around the nodes and then press **C** on the keyboard. Alternatively, control-click any of the selected nodes and then choose **Add Comment**.

![A screenshot showing a comment box added around multiple selected nodes in the Reality Composer Pro Graph Editor.](https://docs-assets.developer.apple.com/published/6595af9f5eb6de95ff844f03e8e98218/CommentBox%402x.png)

After you add a comment, control-click it to open its context menu and do any of the following:

- Cut, copy, or paste a comment and its associated nodes.
- Choose **Delete** to delete only the comment. The associated nodes remain.
- Choose **Duplicate** to duplicate the comment and its contents (nodes). Although the duplicate includes the nodes from the original comment, those nodes aren’t connected to anything.
- Click the ellipsis (…) button and then choose **Change Color** to open a color selector and change the color, opacity, and other visual characteristics for the comment.

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Navigate the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Reuse a single asset across many scene placements by editing prototypes once and propagating the changes to every instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-grapheditoroverview)*