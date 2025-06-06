# mutableCopy(with:)

**Framework**: AVFoundation  
**Kind**: method

Creates a mutable copy of a caption region.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func mutableCopy(with zone: NSZone? = nil) -> Any
```

#### Return Value

A copy of the region.

#### Discussion

This method throws an exception if the caption region contains an identifier.

## Parameters

- `zone`: The system ignores this parameter. Objective-C doesn’t no longer supports memory zones.

## See Also

- [func encode(with: NSCoder)](avcaptionregion/encode(with:).md)
  Encodes the region using the specified encoder.
- [func isEqual(Any) -> Bool](avcaptionregion/isequal(_:).md)
  Returns a Boolean value that indicates whether an object equals another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/mutablecopy(with:))*