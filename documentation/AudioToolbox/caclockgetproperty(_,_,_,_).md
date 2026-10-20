# CAClockGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetProperty(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus CAClockGetProperty(CAClockRef inCAClock, CAClockPropertyID inPropertyID, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

## See Also

### Accessing Clock Properties
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./caclockgetpropertyinfo%28_,_,_,_%29.md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./caclocksetproperty%28_,_,_,_%29.md)
- [enum CAClockPropertyID](./caclockpropertyid.md)
- [enum CAClockSyncMode](./caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetproperty(_:_:_:_:))*