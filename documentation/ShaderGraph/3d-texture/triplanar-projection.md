# Triplanar Projection

**Framework**: ShaderGraph  
**Kind**: subscript

Samples data from three images and projects each along its respective coordinate axis and blends them by geometric normal.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Description

#### Discussion

Use the `Triplanar Projection` node to blend three different images together based on the vector normal of each point on the object. Areas of the object that are parallel with a coordinate axis cause the node to fully show the respective image. Areas of the object between the coordinate axis cause the node to render a mix of the images based on how close the normal is to each of the axis. The closer the normal is to the normal of a coordinate axis the strong the respective image is in the blend. Below is an example of a simple node graph that uses the `Triplanar Projection` node to blend the same grass image in the X and Y directions, and a tile texture in the Z direction:

![None](https://docs-assets.developer.apple.com/published/6eb46ff8978c7668db66854d9c28a713/TriplanarGraph.png)

Below, the resulting texture applies to a sphere:

![None](https://docs-assets.developer.apple.com/published/1117a45d6a0935576157ebc4b3f41684/TriplanarMaterial.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-texture/triplanar-projection)*