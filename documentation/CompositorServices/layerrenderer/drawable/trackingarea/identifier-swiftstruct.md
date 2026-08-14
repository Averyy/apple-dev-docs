# LayerRenderer.Drawable.TrackingArea.Identifier

**Framework**: Compositor Services  
**Kind**: struct

An identifier for the tracking area.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Identifier
```

#### Overview

All tracking areas should have a unique value in a frame. This value should be constant for the same rendered mesh/object across frames to ensure tracking areas are identifiable between frames. There is no reserved values so all values are considered valid but should be unique.

## Topics

### Initializers
- [init(UInt64)](layerrenderer/drawable/trackingarea/identifier-swift.struct/init(_:).md)
- [init(rawValue: UInt64)](layerrenderer/drawable/trackingarea/identifier-swift.struct/init(rawvalue:).md)
### Type Properties
- [static let invalid: LayerRenderer.Drawable.TrackingArea.Identifier](layerrenderer/drawable/trackingarea/identifier-swift.struct/invalid.md)
  Identifier reserved as invalid.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/trackingarea/identifier-swift.struct)*