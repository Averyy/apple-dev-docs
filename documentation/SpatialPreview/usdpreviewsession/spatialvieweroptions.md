# USDPreviewSession.SpatialViewerOptions

**Framework**: Spatial Preview  
**Kind**: struct  
**Role**: Structure

Configuration options that control interaction capabilities for a USD document session.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
struct SpatialViewerOptions
```

## Overview

Use these options to specify what features are available to users during a remote preview session. Options can be combined using standard `OptionSet` syntax to create custom configurations.

## Topics

### Instance Properties
- [var description: String](./spatialvieweroptions/description.md)
  A human-readable description of the enabled options.
### Type Properties
- [static let annotations: USDPreviewSession.SpatialViewerOptions](./spatialvieweroptions/annotations.md)
  Enables annotation capabilities during the `USDPreviewSession`.
- [static let `default`: USDPreviewSession.SpatialViewerOptions](./spatialvieweroptions/default.md)
  The default configuration enabling all available interaction capabilities.
- [static let export: USDPreviewSession.SpatialViewerOptions](./spatialvieweroptions/export.md)
  Enables export capabilities during the `USDPreviewSession`
- [static let perObjectManipulation: USDPreviewSession.SpatialViewerOptions](./spatialvieweroptions/perobjectmanipulation.md)
  Enables per-object manipulation capabilities during the `USDPreviewSession`.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/spatialvieweroptions)*