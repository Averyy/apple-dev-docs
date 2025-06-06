# encode(with:)

**Framework**: AVFoundation  
**Kind**: method

Encodes the region using the specified encoder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func encode(with encoder: NSCoder)
```

#### Discussion

This method throws an exception if the caption region’s [`size`](avcaptionregion/size.md) has different units for [`width`](avcaptionsize/width.md) and [`height`](avcaptionsize/height.md), or if the units are unrecognizeable.

## Parameters

- `encoder`: An encoder instance to use.

## See Also

- [func mutableCopy(with: NSZone?) -> Any](avcaptionregion/mutablecopy(with:).md)
  Creates a mutable copy of a caption region.
- [func isEqual(Any) -> Bool](avcaptionregion/isequal(_:).md)
  Returns a Boolean value that indicates whether an object equals another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/encode(with:))*