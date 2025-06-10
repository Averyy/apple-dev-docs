# PreviewCamera

**Framework**: DeveloperToolsSupport  
**Kind**: struct

A camera that defines a viewpoint in a preview.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct PreviewCamera
```

#### Overview

Use one or more preview cameras with one of the preview macros that takes a `cameras` input — like [`Preview(_:traits:body:cameras:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:traits:body:cameras:)) — to create custom viewpoints for the preview. The canvas offers custom cameras in its camera picker along with a set of standard cameras. The preview uses the first custom camera that you specify as the default viewpoint when the preview appears.

For example, you can create custom cameras from the top, leading, and front viewpoints:

```swift
#Preview {
    CircleImage()
} cameras: {
    PreviewCamera(from: .top, name: "Top")
    PreviewCamera(from: .leading, name: "Leading")
    PreviewCamera(from: .front, name: "Front")
}
```

## Topics

### Initializers
- [init(from: UnitPoint3D, zoom: Double, name: String?)](previewcamera/init(from:zoom:name:).md)
  Creates a camera that looks toward the preview center from a specified unit point.
- [init(lookingAt: Point3D, from: Point3D, name: String?)](previewcamera/init(lookingat:from:name:).md)
  Creates a camera that looks towards a specified point in the preview from a different specified point.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PreviewCameraBuilder](previewcamerabuilder.md)
  A builder type that composes a collection of cameras for previewing a view in a 3D scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamera)*