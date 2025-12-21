# isHostTimeValid

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

This property returns [`true`](https://developer.apple.com/documentation/Swift/true) if the [`hostTime`](avaudiotime/hosttime.md) property is valid; otherwise, it returns [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var hostTime: UInt64](avaudiotime/hosttime.md)
  The host time.
- [class func hostTime(forSeconds: TimeInterval) -> UInt64](avaudiotime/hosttime(forseconds:).md)
  Converts seconds to host time.
- [class func seconds(forHostTime: UInt64) -> TimeInterval](avaudiotime/seconds(forhosttime:).md)
  Converts host time to seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/ishosttimevalid)*