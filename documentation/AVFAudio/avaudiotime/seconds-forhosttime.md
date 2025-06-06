# seconds(forHostTime:)

**Framework**: AVFAudio  
**Kind**: method

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

#### Return Value

The number of seconds that represent the host time you specify.

## Parameters

- `hostTime`: The host time.

## See Also

- [var hostTime: UInt64](avaudiotime/hosttime.md)
  The host time.
- [var isHostTimeValid: Bool](avaudiotime/ishosttimevalid.md)
  A Boolean value that indicates whether the host time value is valid.
- [class func hostTime(forSeconds: TimeInterval) -> UInt64](avaudiotime/hosttime(forseconds:).md)
  Converts seconds to host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/seconds(forhosttime:))*