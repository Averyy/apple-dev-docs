# mutableCopy(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) mutableCopyWithZone:(NSZone *) zone;
```

## Return Value

A copy of the region.

## Discussion

This method throws an exception if the caption region contains an identifier.

## Parameters

- `zone`: The system ignores this parameter. Objective-C doesn’t no longer supports memory zones.

## See Also

### Processing regions
- [func encode(with: NSCoder)](./encode%28with%29.md)
  Encodes the region using the specified encoder.
- [func isEqual(Any) -> Bool](./isequal%28_%29.md)
  Returns a Boolean value that indicates whether an object equals another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/mutablecopy(with:))*