# isHostTimeValid

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the host time value is valid.

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
var isHostTimeValid: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isHostTimeValid) BOOL hostTimeValid;
```

## Discussion

This property returns [`true`](../../Swift/true.md) if the [`hostTime`](./hosttime.md) property is valid; otherwise, it returns [`false`](../../Swift/false.md).

## See Also

### Manipulating host time
- [var hostTime: UInt64](./hosttime.md)
  The host time.
- [class func hostTime(forSeconds: TimeInterval) -> UInt64](./hosttime%28forseconds%29.md)
  Converts seconds to host time.
- [class func seconds(forHostTime: UInt64) -> TimeInterval](./seconds%28forhosttime%29.md)
  Converts host time to seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/ishosttimevalid)*