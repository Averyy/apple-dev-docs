# AudioFileComponentCountUserData(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentCountUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ outNumberItems: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetuserdata(_:_:_:_:_:).md)
- [func AudioFileComponentSetUserData(AudioFileComponent, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetuserdata(_:_:_:_:_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcountuserdata(_:_:_:))*