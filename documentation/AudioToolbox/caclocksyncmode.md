# CAClockSyncMode

**Framework**: Audio Toolbox  
**Kind**: enum

**Availability**:
- macOS ?+

## Declaration

```swift
enum CAClockSyncMode
```

## Topics

### Constants
- [CAClockSyncMode.internal](caclocksyncmode/internal.md)
- [CAClockSyncMode.midiClockTransport](caclocksyncmode/midiclocktransport.md)
- [CAClockSyncMode.mtcTransport](caclocksyncmode/mtctransport.md)
### Initializers
- [init?(rawValue: UInt32)](caclocksyncmode/init(rawvalue:).md)

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
- [enum CAClockPropertyID](caclockpropertyid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksyncmode)*