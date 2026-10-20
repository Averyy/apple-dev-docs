# itemTime(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Converts a Core Video timestamp to the item’s timebase.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func itemTime(for timestamp: CVTimeStamp) -> CMTime
```

```objc
- (CMTime) itemTimeForCVTimeStamp:(CVTimeStamp) timestamp;
```

#### Return Value

The equivalent time in the item’s timebase.

## Parameters

- `timestamp`: A timestamp value provided by the Core Video framework.

## See Also

### Time conversion
- [func itemTime(forHostTime: CFTimeInterval) -> CMTime](./itemtime%28forhosttime%29.md)
  Converts a host time, specified in seconds, to the item’s timebase.
- [func itemTime(forMachAbsoluteTime: Int64) -> CMTime](./itemtime%28formachabsolutetime%29.md)
  Converts a Mach host time to the item’s timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(for:))*