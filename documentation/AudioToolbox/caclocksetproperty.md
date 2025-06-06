# CAClockSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetProperty(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

## See Also

- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](caclockgetproperty(_:_:_:_:).md)
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](caclockgetpropertyinfo(_:_:_:_:).md)
- [enum CAClockPropertyID](caclockpropertyid.md)
- [enum CAClockSyncMode](caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetproperty(_:_:_:_:))*