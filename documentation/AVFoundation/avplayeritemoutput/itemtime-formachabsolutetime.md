# itemTime(forMachAbsoluteTime:)

**Framework**: AVFoundation  
**Kind**: method

Converts a Mach host time to the item’s timebase.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func itemTime(forMachAbsoluteTime machAbsoluteTime: Int64) -> CMTime
```

#### Return Value

The equivalent time in the item’s timebase.

## Parameters

- `machAbsoluteTime`: The Mach host time to convert. You typically retrieve this value using the   function.

## See Also

- [func itemTime(forHostTime: CFTimeInterval) -> CMTime](avplayeritemoutput/itemtime(forhosttime:).md)
  Converts a host time, specified in seconds, to the item’s timebase.
- [func itemTime(for: CVTimeStamp) -> CMTime](avplayeritemoutput/itemtime(for:).md)
  Converts a Core Video timestamp to the item’s timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(formachabsolutetime:))*