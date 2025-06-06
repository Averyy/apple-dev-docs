# AudioFileComponentGetUserData(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

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
- [typealias GetUserDataFDF](getuserdatafdf.md)
- [typealias GetUserDataSizeFDF](getuserdatasizefdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdata(_:_:_:_:_:))*