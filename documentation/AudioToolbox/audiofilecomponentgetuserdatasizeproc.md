# AudioFileComponentGetUserDataSizeProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentGetUserDataSizeProc = (UnsafeMutableRawPointer, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, unsigned int *) AudioFileComponentGetUserDataSizeProc;
```

## See Also

### Accessing the User Data
- [func AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetuserdata%28_,_,_,_,_%29.md)
- [func AudioFileComponentSetUserData(AudioFileComponent, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilecomponentsetuserdata%28_,_,_,_,_%29.md)
- [func AudioFileComponentCountUserData(AudioFileComponent, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentcountuserdata%28_,_,_%29.md)
- [func AudioFileComponentGetUserDataSize(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentgetuserdatasize%28_,_,_,_%29.md)
- [func AudioFileComponentRemoveUserData(AudioFileComponent, UInt32, UInt32) -> OSStatus](./audiofilecomponentremoveuserdata%28_,_,_%29.md)
- [typealias AudioFileComponentCountUserDataProc](./audiofilecomponentcountuserdataproc.md)
- [typealias AudioFileComponentGetUserDataProc](./audiofilecomponentgetuserdataproc.md)
- [typealias AudioFileComponentRemoveUserDataProc](./audiofilecomponentremoveuserdataproc.md)
- [typealias AudioFileComponentSetUserDataProc](./audiofilecomponentsetuserdataproc.md)
- [typealias CountUserDataFDF](./countuserdatafdf.md)
- [typealias GetUserDataFDF](./getuserdatafdf.md)
- [typealias GetUserDataSizeFDF](./getuserdatasizefdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdatasizeproc)*