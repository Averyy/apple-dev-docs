# init(from:zoom:name:)

**Framework**: DeveloperToolsSupport  
**Kind**: init  
**Role**: Initializer

Creates a camera that looks toward the preview center from a specified unit point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(from point: UnitPoint3D, zoom: Double = 1, name: String? = nil)
```

#### Discussion

Use one or more cameras with one of the preview macros that takes a `cameras` input — like [`Preview(_:traits:body:cameras:)`](../../SwiftUI/preview%28_,traits,body,cameras%29.md) — to create custom viewpoints for the preview. The canvas offers custom cameras in its camera picker along with a set of standard cameras.

## Parameters

- `point`: The point in 3D space where to place the camera, given as a unit point relative to the preview center.
- `zoom`: An optional amount by which to scale the distance from the camera to the preview center. Values larger than `1` move the camera closer to the preview center. Fractional values move the camera away.
- `name`: An optional name that the canvas uses to label the camera.

## See Also

### Creating a preview camera
- [init(lookingAt: Point3D, from: Point3D, name: String?)](./init%28lookingat,from,name%29.md)
  Creates a camera that looks towards a specified point in the preview from a different specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamera/init(from:zoom:name:))*