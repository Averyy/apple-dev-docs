# CAClockGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockGetPropertyInfo(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ outSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

```c
extern OSStatus CAClockGetPropertyInfo(CAClockRef inCAClock, CAClockPropertyID inPropertyID, UInt32 *outSize, Boolean *outWritable);
```

## See Also

### Accessing Clock Properties
- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./caclockgetproperty%28_,_,_,_%29.md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./caclocksetproperty%28_,_,_,_%29.md)
- [enum CAClockPropertyID](./caclockpropertyid.md)
- [enum CAClockSyncMode](./caclocksyncmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockgetpropertyinfo(_:_:_:_:))*