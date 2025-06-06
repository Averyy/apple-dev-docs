# CAClockPropertyID

**Framework**: Audio Toolbox  
**Kind**: enum

**Availability**:
- macOS ?+

## Declaration

```swift
enum CAClockPropertyID
```

## Topics

### Constants
- [CAClockPropertyID.internalTimebase](caclockpropertyid/internaltimebase.md)
- [CAClockPropertyID.midiClockDestinations](caclockpropertyid/midiclockdestinations.md)
- [CAClockPropertyID.mtcDestinations](caclockpropertyid/mtcdestinations.md)
- [CAClockPropertyID.mtcFreewheelTime](caclockpropertyid/mtcfreewheeltime.md)
- [CAClockPropertyID.meterTrack](caclockpropertyid/metertrack.md)
- [CAClockPropertyID.name](caclockpropertyid/name.md)
- [CAClockPropertyID.smpteFormat](caclockpropertyid/smpteformat.md)
- [CAClockPropertyID.smpteOffset](caclockpropertyid/smpteoffset.md)
- [CAClockPropertyID.sendMIDISPP](caclockpropertyid/sendmidispp.md)
- [CAClockPropertyID.syncMode](caclockpropertyid/syncmode.md)
- [CAClockPropertyID.syncSource](caclockpropertyid/syncsource.md)
- [CAClockPropertyID.tempoMap](caclockpropertyid/tempomap.md)
- [CAClockPropertyID.timebaseSource](caclockpropertyid/timebasesource.md)
### Initializers
- [init?(rawValue: UInt32)](caclockpropertyid/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](caclockgetproperty(_:_:_:_:).md)
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](caclockgetpropertyinfo(_:_:_:_:).md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](caclocksetproperty(_:_:_:_:).md)
- [enum CAClockSyncMode](caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockpropertyid)*