# AVCaptionUnitsType

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

A structure that defines a units for caption formats.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```swift
enum AVCaptionUnitsType
```

```c
enum AVCaptionUnitsType : NSInteger;
```

## Overview

Some geometry values may use sizing and positioning with different units. In some cases, an object might allow multiple kinds of dimensions varying by units.

## Topics

### Unit types
- [AVCaptionUnitsType.cells](./avcaptionunitstype/cells.md)
  A cell-based unit type.
- [AVCaptionUnitsType.percent](./avcaptionunitstype/percent.md)
  A percentage-based unit type.
- [AVCaptionUnitsType.unspecified](./avcaptionunitstype/unspecified.md)
  An unspecified unit type.
### Initializers
- [init?(rawValue: Int)](./avcaptionunitstype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting the dimensions
- [var value: CGFloat](./avcaptiondimension/value.md)
  The value of the coordinate or length.
- [var units: AVCaptionUnitsType](./avcaptiondimension/units.md)
  The units of the coordinate, such as cells or points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionunitstype)*