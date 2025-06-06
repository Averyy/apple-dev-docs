# AVCaptionUnitsType

**Framework**: AVFoundation  
**Kind**: enum

A structure that defines a units for caption formats.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum AVCaptionUnitsType
```

#### Overview

Some geometry values may use sizing and positioning with different units. In some cases, an object might allow multiple kinds of dimensions varying by units.

## Topics

### Unit Types
- [AVCaptionUnitsType.cells](avcaptionunitstype/cells.md)
  A cell-based unit type.
- [AVCaptionUnitsType.percent](avcaptionunitstype/percent.md)
  A percentage-based unit type.
- [AVCaptionUnitsType.unspecified](avcaptionunitstype/unspecified.md)
  An unspecified unit type.
### Initializers
- [init?(rawValue: Int)](avcaptionunitstype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var value: CGFloat](avcaptiondimension/value.md)
  The value of the coordinate or length.
- [var units: AVCaptionUnitsType](avcaptiondimension/units.md)
  The units of the coordinate, such as cells or points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionunitstype)*