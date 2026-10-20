# CAClockPropertyID

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS

## Declaration

```swift
enum CAClockPropertyID
```

```c
enum CAClockPropertyID : UInt32;
```

## Topics

### Constants
- [CAClockPropertyID.internalTimebase](./caclockpropertyid/internaltimebase.md)
- [CAClockPropertyID.midiClockDestinations](./caclockpropertyid/midiclockdestinations.md)
- [CAClockPropertyID.mtcDestinations](./caclockpropertyid/mtcdestinations.md)
- [CAClockPropertyID.mtcFreewheelTime](./caclockpropertyid/mtcfreewheeltime.md)
- [CAClockPropertyID.meterTrack](./caclockpropertyid/metertrack.md)
- [CAClockPropertyID.name](./caclockpropertyid/name.md)
- [CAClockPropertyID.smpteFormat](./caclockpropertyid/smpteformat.md)
- [CAClockPropertyID.smpteOffset](./caclockpropertyid/smpteoffset.md)
- [CAClockPropertyID.sendMIDISPP](./caclockpropertyid/sendmidispp.md)
- [CAClockPropertyID.syncMode](./caclockpropertyid/syncmode.md)
- [CAClockPropertyID.syncSource](./caclockpropertyid/syncsource.md)
- [CAClockPropertyID.tempoMap](./caclockpropertyid/tempomap.md)
- [CAClockPropertyID.timebaseSource](./caclockpropertyid/timebasesource.md)
### Initializers
- [init?(rawValue: UInt32)](./caclockpropertyid/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Clock Properties
- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./caclockgetproperty%28_,_,_,_%29.md)
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./caclockgetpropertyinfo%28_,_,_,_%29.md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./caclocksetproperty%28_,_,_,_%29.md)
- [enum CAClockSyncMode](./caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockpropertyid)*