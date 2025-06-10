# Placing a prim in the real world

**Framework**: RealityKit

Anchor a prim to a real-world object that the runtime recognizes in the physical environment.

#### Overview

When the runtime detects real-world landmarks such as surfaces, images, and faces, it keeps tabs on them in case the app needs to refer to them later as data points for adding virtual content. To track a landmark, the runtime assigns an anchor and updates it to track the orientation and position of that landmark while it’s visible in the camera feed.

Use this schema to attach prims to anchors that the runtime can recognize and track in the physical environment. When you assign the prim an anchor type, the runtime places the prim on the first anchor of that type that it sees in the AR experience.

> **Note**:  When a RealityKit app loads an anchored prim with `loadAnchor(named:in:)`, RealityKit instantiates an [`AnchorEntity`](AnchorEntity.md) with the [`AnchoringComponent.Target`](AnchoringComponent/Target-swift.enum.md) set to the anchor type specified by the prim, such as a plane, image, or face.

##### Place a Prim on a Surface Image or Face

The following cube requests that the runtime place it on the first real-world horizontal surface detected in the physical environment.

```other
def Cube "PlaneAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "plane"
    uniform token preliminary:planeAnchoring:alignment = "horizontal"
    ...
}
```

The cube defined in the following example sends a request to the runtime to place it at the real-world location of an image described by `image.png`.

```other
def Cube "ImageAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "image"
    rel preliminary:imageAnchoring:referenceImage = <ImageReference>
    ...

    def Preliminary_ReferenceImage "ImageReference"
    {
      uniform asset image = @image.png@
      uniform double physicalWidth = 0.12
    }
}

```

The following example instructs the runtime to place a cube at the real-word location of a detected face. In RealityKit, a face anchor centers its content at its origin, which is the detected face’s plane midpoint.

```other
def Cube "FaceAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "face"
    ...
}

```

## See Also

- [Preliminary_AnchoringAPI](preliminary-anchoringapi.md)
  A schema that defines the placement of a prim and its children at a real-world location.
- [Preliminary_ReferenceImage](preliminary-referenceimage.md)
  A schema that defines the properties of an image in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/placing-a-prim-in-the-real-world)*