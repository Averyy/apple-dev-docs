# CAClockSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockSetProperty(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

```c
extern OSStatus CAClockSetProperty(CAClockRef inCAClock, CAClockPropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

## See Also

### Accessing Clock Properties
- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./caclockgetproperty%28_,_,_,_%29.md)
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./caclockgetpropertyinfo%28_,_,_,_%29.md)
- [enum CAClockPropertyID](./caclockpropertyid.md)
- [enum CAClockSyncMode](./caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocksetproperty(_:_:_:_:))*