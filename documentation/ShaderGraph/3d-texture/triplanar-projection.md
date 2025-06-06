# Triplanar Projection

**Framework**: ShaderGraph  
**Kind**: subscript

Samples data from three images and projects each along its respective coordinate axis and blends them by geometric normal.

#### Parameter Types

#### Parameter Description

#### Discussion

The Triplanar Projection node is used to blend three different images together based on the vector normal of each point on the object. Areas of the object that are parallel with a coordinate axis will cause the node to fully show the respective image. Areas of the object that are in between the coordinate axis will cause the node to render a mix of the images based on how close the normal is to each of the axis. The closer the normal is to being the normal of a coordinate axis the strong the respective image will be in the blend. Below is an example of a simple node graph that uses the Triplanar Projection node to blend the same grass image in the  and  directions and a tile texture in the  direction.

![None](https://docs-assets.developer.apple.com/published/6eb46ff8978c7668db66854d9c28a713/TriplanarGraph.png)

Below, the resulting texture applies to a sphere.

![None](https://docs-assets.developer.apple.com/published/1117a45d6a0935576157ebc4b3f41684/TriplanarMaterial.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-texture/triplanar-projection)*