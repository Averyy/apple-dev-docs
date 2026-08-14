# USDPreviewSession.SpatialViewerOptions

**Framework**: Spatial Preview  
**Kind**: struct

Configuration options that control interaction capabilities for a USD document session.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct SpatialViewerOptions
```

#### Overview

Use these options to specify what features are available to users during a remote preview session. Options can be combined using standard `OptionSet` syntax to create custom configurations.

## Topics

### Instance Properties
- [var description: String](usdpreviewsession/spatialvieweroptions/description.md)
  A human-readable description of the enabled options.
### Type Properties
- [static let annotations: USDPreviewSession.SpatialViewerOptions](usdpreviewsession/spatialvieweroptions/annotations.md)
  Enables annotation capabilities during the `USDPreviewSession`.
- [static let `default`: USDPreviewSession.SpatialViewerOptions](usdpreviewsession/spatialvieweroptions/default.md)
  The default configuration enabling all available interaction capabilities.
- [static let export: USDPreviewSession.SpatialViewerOptions](usdpreviewsession/spatialvieweroptions/export.md)
  Enables export capabilities during the `USDPreviewSession`
- [static let perObjectManipulation: USDPreviewSession.SpatialViewerOptions](usdpreviewsession/spatialvieweroptions/perobjectmanipulation.md)
  Enables per-object manipulation capabilities during the `USDPreviewSession`.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/spatialvieweroptions)*