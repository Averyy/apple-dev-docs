# CAClockGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetProperty(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](caclockgetpropertyinfo(_:_:_:_:).md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](caclocksetproperty(_:_:_:_:).md)
- [enum CAClockPropertyID](caclockpropertyid.md)
- [enum CAClockSyncMode](caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetproperty(_:_:_:_:))*