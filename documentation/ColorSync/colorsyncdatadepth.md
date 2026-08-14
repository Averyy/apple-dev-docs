# ColorSyncDataDepth

**Framework**: ColorSync  
**Kind**: struct

The bit depth and numeric type of a color component in a pixel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ColorSyncDataDepth
```

## Topics

### Initializers
- [init(UInt32)](colorsyncdatadepth/init(_:).md)
- [init(rawValue: UInt32)](colorsyncdatadepth/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](colorsyncdatadepth/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct ColorSyncAlphaInfo](colorsyncalphainfo.md)
  The location of the alpha component in a pixel, and whether it’s premultiplied.
- [typealias ColorSyncDataLayout](colorsyncdatalayout.md)
  A bit field describing the alpha information and byte order of a pixel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncdatadepth)*