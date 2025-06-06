# hostTime(forSeconds:)

**Framework**: AVFAudio  
**Kind**: method

Converts seconds to host time.

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
class func hostTime(forSeconds seconds: TimeInterval) -> UInt64
```

#### Return Value

The host time that represents the seconds you specify.

## Parameters

- `seconds`: The number of seconds.

## See Also

- [var hostTime: UInt64](avaudiotime/hosttime.md)
  The host time.
- [var isHostTimeValid: Bool](avaudiotime/ishosttimevalid.md)
  A Boolean value that indicates whether the host time value is valid.
- [class func seconds(forHostTime: UInt64) -> TimeInterval](avaudiotime/seconds(forhosttime:).md)
  Converts host time to seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/hosttime(forseconds:))*