# hostTime

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The host time.

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
var hostTime: UInt64 { get }
```

```objc
@property (nonatomic, readonly) uint64_t hostTime;
```

## See Also

### Manipulating host time
- [var isHostTimeValid: Bool](./ishosttimevalid.md)
  A Boolean value that indicates whether the host time value is valid.
- [class func hostTime(forSeconds: TimeInterval) -> UInt64](./hosttime%28forseconds%29.md)
  Converts seconds to host time.
- [class func seconds(forHostTime: UInt64) -> TimeInterval](./seconds%28forhosttime%29.md)
  Converts host time to seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/hosttime)*