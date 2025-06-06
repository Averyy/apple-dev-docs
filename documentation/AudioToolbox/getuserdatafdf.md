# GetUserDataFDF

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias GetUserDataFDF = (UnsafeMutableRawPointer, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetuserdata(_:_:_:_:_:).md)
- [func AudioFileComponentSetUserData(AudioFileComponent, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetuserdata(_:_:_:_:_:).md)
- [func AudioFileComponentCountUserData(AudioFileComponent, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentcountuserdata(_:_:_:).md)
- [func AudioFileComponentGetUserDataSize(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentgetuserdatasize(_:_:_:_:).md)
- [func AudioFileComponentRemoveUserData(AudioFileComponent, UInt32, UInt32) -> OSStatus](audiofilecomponentremoveuserdata(_:_:_:).md)
- [typealias AudioFileComponentCountUserDataProc](audiofilecomponentcountuserdataproc.md)
- [typealias AudioFileComponentGetUserDataProc](audiofilecomponentgetuserdataproc.md)
- [typealias AudioFileComponentGetUserDataSizeProc](audiofilecomponentgetuserdatasizeproc.md)
- [typealias AudioFileComponentRemoveUserDataProc](audiofilecomponentremoveuserdataproc.md)
- [typealias AudioFileComponentSetUserDataProc](audiofilecomponentsetuserdataproc.md)
- [typealias CountUserDataFDF](countuserdatafdf.md)
- [typealias GetUserDataSizeFDF](getuserdatasizefdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/getuserdatafdf)*