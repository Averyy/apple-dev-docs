# CAClockTimeFormat

**Framework**: Audio Toolbox  
**Kind**: enum

**Availability**:
- macOS ?+

## Declaration

```swift
enum CAClockTimeFormat
```

## Topics

### Constants
- [CAClockTimeFormat.absoluteSeconds](caclocktimeformat/absoluteseconds.md)
- [CAClockTimeFormat.beats](caclocktimeformat/beats.md)
- [CAClockTimeFormat.hostTime](caclocktimeformat/hosttime.md)
- [CAClockTimeFormat.smpteSeconds](caclocktimeformat/smpteseconds.md)
- [CAClockTimeFormat.smpteTime](caclocktimeformat/smptetime.md)
- [CAClockTimeFormat.samples](caclocktimeformat/samples.md)
- [CAClockTimeFormat.seconds](caclocktimeformat/seconds.md)
### Initializers
- [init?(rawValue: UInt32)](caclocktimeformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetcurrenttime(_:_:_:).md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](caclocksetcurrenttime(_:_:).md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetstarttime(_:_:_:).md)
- [struct CAClockTime](caclocktime.md)
- [typealias CAClockSamples](caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocktimeformat)*