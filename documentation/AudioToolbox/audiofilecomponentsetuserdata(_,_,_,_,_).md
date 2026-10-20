# AudioFileComponentSetUserData(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentSetUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: UnsafeRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentSetUserData(AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt32 inUserDataSize, const void *inUserData);
```

## See Also

### Accessing the User Data
- [func AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetuserdata%28_,_,_,_,_%29.md)
- [func AudioFileComponentCountUserData(AudioFileComponent, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentcountuserdata%28_,_,_%29.md)
- [func AudioFileComponentGetUserDataSize(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentgetuserdatasize%28_,_,_,_%29.md)
- [func AudioFileComponentRemoveUserData(AudioFileComponent, UInt32, UInt32) -> OSStatus](./audiofilecomponentremoveuserdata%28_,_,_%29.md)
- [typealias AudioFileComponentCountUserDataProc](./audiofilecomponentcountuserdataproc.md)
- [typealias AudioFileComponentGetUserDataProc](./audiofilecomponentgetuserdataproc.md)
- [typealias AudioFileComponentGetUserDataSizeProc](./audiofilecomponentgetuserdatasizeproc.md)
- [typealias AudioFileComponentRemoveUserDataProc](./audiofilecomponentremoveuserdataproc.md)
- [typealias AudioFileComponentSetUserDataProc](./audiofilecomponentsetuserdataproc.md)
- [typealias CountUserDataFDF](./countuserdatafdf.md)
- [typealias GetUserDataFDF](./getuserdatafdf.md)
- [typealias GetUserDataSizeFDF](./getuserdatasizefdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentsetuserdata(_:_:_:_:_:))*