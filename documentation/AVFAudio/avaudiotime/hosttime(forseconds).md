# hostTime(forSeconds:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (uint64_t) hostTimeForSeconds:(NSTimeInterval) seconds;
```

#### Return Value

The host time that represents the seconds you specify.

## Parameters

- `seconds`: The number of seconds.

## See Also

### Manipulating host time
- [var hostTime: UInt64](./hosttime.md)
  The host time.
- [var isHostTimeValid: Bool](./ishosttimevalid.md)
  A Boolean value that indicates whether the host time value is valid.
- [class func seconds(forHostTime: UInt64) -> TimeInterval](./seconds%28forhosttime%29.md)
  Converts host time to seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/hosttime(forseconds:))*