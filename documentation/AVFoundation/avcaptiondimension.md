# AVCaptionDimension

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines a caption dimension.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```swift
struct AVCaptionDimension
```

```c
typedef struct AVCaptionDimension { ... } AVCaptionDimension;
```

## Topics

### Inspecting the dimensions
- [var value: CGFloat](./avcaptiondimension/value.md)
  The value of the coordinate or length.
- [var units: AVCaptionUnitsType](./avcaptiondimension/units.md)
  The units of the coordinate, such as cells or points.
- [enum AVCaptionUnitsType](./avcaptionunitstype.md)
  A structure that defines a units for caption formats.
### Initializers
- [init()](./avcaptiondimension/init%28%29.md)
  Creates a caption dimension.
- [init(value: CGFloat, units: AVCaptionUnitsType)](./avcaptiondimension/init%28value,units%29.md)
  Creates a caption dimension with a value and unit type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiondimension)*