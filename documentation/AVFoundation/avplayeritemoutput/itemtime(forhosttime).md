# itemTime(forHostTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Converts a host time, specified in seconds, to the item’s timebase.

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
func itemTime(forHostTime hostTimeInSeconds: CFTimeInterval) -> CMTime
```

```objc
- (CMTime) itemTimeForHostTime:(CFTimeInterval) hostTimeInSeconds;
```

#### Return Value

The equivalent time in the item’s timebase.

#### Discussion

The timestamp associated with a [`CADisplayLink`](../../QuartzCore/cadisplaylink.md) object represents the time of the most recent screen refresh, which is usually a time in the past. If you want to find the time associated with the next screen refresh, you need to increment the timestamp by the value in the display link’s `duration` property.

## Parameters

- `hostTimeInSeconds`: A host time value, specified in seconds. For example, you might specify the time value returned by the [`CACurrentMediaTime()`](../../QuartzCore/cacurrentmediatime%28%29.md) function or the timestamp from a [`CADisplayLink`](../../QuartzCore/cadisplaylink.md) object for this parameter.

## See Also

### Time conversion
- [func itemTime(forMachAbsoluteTime: Int64) -> CMTime](./itemtime%28formachabsolutetime%29.md)
  Converts a Mach host time to the item’s timebase.
- [func itemTime(for: CVTimeStamp) -> CMTime](./itemtime%28for%29.md)
  Converts a Core Video timestamp to the item’s timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(forhosttime:))*