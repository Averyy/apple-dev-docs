# seconds(forHostTime:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

Converts host time to seconds.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func seconds(forHostTime hostTime: UInt64) -> TimeInterval
```

```objc
+ (NSTimeInterval) secondsForHostTime:(uint64_t) hostTime;
```

## Return Value

The number of seconds that represent the host time you specify.

## Parameters

- `hostTime`: The host time.

## See Also

### Manipulating host time
- [var hostTime: UInt64](./hosttime.md)
  The host time.
- [var isHostTimeValid: Bool](./ishosttimevalid.md)
  A Boolean value that indicates whether the host time value is valid.
- [class func hostTime(forSeconds: TimeInterval) -> UInt64](./hosttime%28forseconds%29.md)
  Converts seconds to host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/seconds(forhosttime:))*