# PreviewCameraBuilder

**Framework**: DeveloperToolsSupport  
**Kind**: struct

A builder type that composes a collection of cameras for previewing a view in a 3D scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct PreviewCameraBuilder
```

#### Overview

You implicitly use a preview camera builder when you define a list of [`PreviewCamera`](previewcamera.md) instances for a preview macro:

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

### Type Methods
- [static func buildArray([[PreviewCamera]]) -> [PreviewCamera]](previewcamerabuilder/buildarray(_:).md)
  Builds a partial result from an array of partial results.
- [static func buildExpression(PreviewCamera) -> [PreviewCamera]](previewcamerabuilder/buildexpression(_:)-5okdh.md)
  Builds a partial result from a single camera.
- [static func buildExpression([PreviewCamera]) -> [PreviewCamera]](previewcamerabuilder/buildexpression(_:)-5t9d2.md)
  Builds a partial result from an array of cameras.
- [static func buildPartialBlock(accumulated: [PreviewCamera], next: [PreviewCamera]) -> [PreviewCamera]](previewcamerabuilder/buildpartialblock(accumulated:next:).md)
  Combines an accumulated component with a new component.
- [static func buildPartialBlock(first: [PreviewCamera]) -> [PreviewCamera]](previewcamerabuilder/buildpartialblock(first:).md)
  Builds a partial result component from the first component.

## See Also

- [struct PreviewCamera](previewcamera.md)
  A camera that defines a viewpoint in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamerabuilder)*