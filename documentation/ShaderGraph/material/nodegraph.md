# NodeGraph

**Framework**: Shadergraph  
**Kind**: subscript

A node that can contain shading nodes and other node graphs.

#### Discussion

The NodeGraph node holds other node graphs that can be used in other materials. Use this node to define subgraphs that you commonly use and repeat. The NodeGraph node is a custom node that can be used in all of your other materials.

The graphs in each NodeGraph node function almost exactly the same as the node graph for a custom material, and both use the same set of supported nodes. The main difference is that in a node graph, you can define any number of custom inputs or outputs. Name and define the type for each custom input and output.

> **Note**: The names of any inputs or outputs can’t have spaces in them.

Below is an example of a subgraph defined by a NodeGraph node and an example of using the NodeGraph node in a material. The subgraph takes inputs for horizontal and vertical speeds and outputs texture coordinates that cause an image to scroll either vertically, horizontally, or both. The subgraph is then used to make an arrow image scroll diagonally.

Below the texture applies to a cube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/material/nodegraph)*