# CAClockSyncMode

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS

## Declaration

```swift
enum CAClockSyncMode
```

```c
enum CAClockSyncMode : UInt32;
```

## Topics

### Constants
- [CAClockSyncMode.internal](./caclocksyncmode/internal.md)
- [CAClockSyncMode.midiClockTransport](./caclocksyncmode/midiclocktransport.md)
- [CAClockSyncMode.mtcTransport](./caclocksyncmode/mtctransport.md)
### Initializers
- [init?(rawValue: UInt32)](./caclocksyncmode/init%28rawvalue%29.md)

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
- [enum CAClockPropertyID](./caclockpropertyid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksyncmode)*