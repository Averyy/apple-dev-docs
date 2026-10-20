# AudioFileComponentCountUserData(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentCountUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ outNumberItems: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioFileComponentCountUserData(AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 *outNumberItems);
```

## See Also

### Accessing the User Data
- [func AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetuserdata%28_,_,_,_,_%29.md)
- [func AudioFileComponentSetUserData(AudioFileComponent, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilecomponentsetuserdata%28_,_,_,_,_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcountuserdata(_:_:_:))*