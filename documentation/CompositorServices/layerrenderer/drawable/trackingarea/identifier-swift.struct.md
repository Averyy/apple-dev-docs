# LayerRenderer.Drawable.TrackingArea.Identifier

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

An identifier for the tracking area.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Identifier
```

```c
typedef uint64_t cp_tracking_area_identifier;
```

#### Overview

All tracking areas should have a unique value in a frame. This value should be constant for the same rendered mesh/object across frames to ensure tracking areas are identifiable between frames. There is no reserved values so all values are considered valid but should be unique.

## Topics

### Initializers
- [init(UInt64)](./identifier-swift.struct/init%28_%29.md)
- [init(rawValue: UInt64)](./identifier-swift.struct/init%28rawvalue%29.md)
### Type Properties
- [static let invalid: LayerRenderer.Drawable.TrackingArea.Identifier](./identifier-swift.struct/invalid.md)
  Identifier reserved as invalid.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../../Swift/bitwisecopyable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/trackingarea/identifier-swift.struct)*