# itemTime(for:)

**Framework**: AVFoundation  
**Kind**: method

Converts a Core Video timestamp to the item’s timebase.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func itemTime(for timestamp: CVTimeStamp) -> CMTime
```

#### Return Value

The equivalent time in the item’s timebase.

## Parameters

- `timestamp`: A timestamp value provided by the Core Video framework.

## See Also

- [func itemTime(forHostTime: CFTimeInterval) -> CMTime](avplayeritemoutput/itemtime(forhosttime:).md)
  Converts a host time, specified in seconds, to the item’s timebase.
- [func itemTime(forMachAbsoluteTime: Int64) -> CMTime](avplayeritemoutput/itemtime(formachabsolutetime:).md)
  Converts a Mach host time to the item’s timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(for:))*