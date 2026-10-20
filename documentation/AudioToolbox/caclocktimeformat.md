# CAClockTimeFormat

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS

## Declaration

```swift
enum CAClockTimeFormat
```

```c
enum CAClockTimeFormat : UInt32;
```

## Topics

### Constants
- [CAClockTimeFormat.absoluteSeconds](./caclocktimeformat/absoluteseconds.md)
- [CAClockTimeFormat.beats](./caclocktimeformat/beats.md)
- [CAClockTimeFormat.hostTime](./caclocktimeformat/hosttime.md)
- [CAClockTimeFormat.smpteSeconds](./caclocktimeformat/smpteseconds.md)
- [CAClockTimeFormat.smpteTime](./caclocktimeformat/smptetime.md)
- [CAClockTimeFormat.samples](./caclocktimeformat/samples.md)
- [CAClockTimeFormat.seconds](./caclocktimeformat/seconds.md)
### Initializers
- [init?(rawValue: UInt32)](./caclocktimeformat/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing the Current Time
- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetcurrenttime%28_,_,_%29.md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](./caclocksetcurrenttime%28_,_%29.md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetstarttime%28_,_,_%29.md)
- [struct CAClockTime](./caclocktime.md)
- [typealias CAClockSamples](./caclocksamples.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocktimeformat)*