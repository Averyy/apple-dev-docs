# buildArray(_:)

**Framework**: DeveloperToolsSupport  
**Kind**: method  
**Role**: Type Method

Builds a partial result from an array of partial results.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func buildArray(_ components: [[PreviewCamera]]) -> [PreviewCamera]
```

## See Also

### Building a preview camera
- [static func buildExpression(PreviewCamera) -> [PreviewCamera]](./buildexpression%28_%29-5okdh.md)
  Builds a partial result from a single camera.
- [static func buildExpression([PreviewCamera]) -> [PreviewCamera]](./buildexpression%28_%29-5t9d2.md)
  Builds a partial result from an array of cameras.
- [static func buildPartialBlock(accumulated: [PreviewCamera], next: [PreviewCamera]) -> [PreviewCamera]](./buildpartialblock%28accumulated,next%29.md)
  Combines an accumulated component with a new component.
- [static func buildPartialBlock(first: [PreviewCamera]) -> [PreviewCamera]](./buildpartialblock%28first%29.md)
  Builds a partial result component from the first component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamerabuilder/buildarray(_:))*