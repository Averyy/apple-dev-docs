# PreviewCameraBuilder

**Framework**: DeveloperToolsSupport  
**Kind**: struct  
**Role**: Structure

A builder type that composes a collection of cameras for previewing a view in a 3D scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct PreviewCameraBuilder
```

## Overview

You implicitly use a preview camera builder when you define a list of [`PreviewCamera`](./previewcamera.md) instances for a preview macro:

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

### Building a preview camera
- [static func buildArray([[PreviewCamera]]) -> [PreviewCamera]](./previewcamerabuilder/buildarray%28_%29.md)
  Builds a partial result from an array of partial results.
- [static func buildExpression(PreviewCamera) -> [PreviewCamera]](./previewcamerabuilder/buildexpression%28_%29-5okdh.md)
  Builds a partial result from a single camera.
- [static func buildExpression([PreviewCamera]) -> [PreviewCamera]](./previewcamerabuilder/buildexpression%28_%29-5t9d2.md)
  Builds a partial result from an array of cameras.
- [static func buildPartialBlock(accumulated: [PreviewCamera], next: [PreviewCamera]) -> [PreviewCamera]](./previewcamerabuilder/buildpartialblock%28accumulated,next%29.md)
  Combines an accumulated component with a new component.
- [static func buildPartialBlock(first: [PreviewCamera]) -> [PreviewCamera]](./previewcamerabuilder/buildpartialblock%28first%29.md)
  Builds a partial result component from the first component.

## See Also

### Preview camera management
- [struct PreviewCamera](./previewcamera.md)
  A camera that defines a viewpoint in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamerabuilder)*