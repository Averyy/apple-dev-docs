# AudioFileComponentGetUserDataSize64Proc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentGetUserDataSize64Proc = (UnsafeMutableRawPointer, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, unsigned long long *) AudioFileComponentGetUserDataSize64Proc;
```

## See Also

### Data Types
- [typealias AUMIDIEventListBlock](./aumidieventlistblock.md)
- [typealias AudioFileComponentGetUserDataAtOffsetProc](./audiofilecomponentgetuserdataatoffsetproc.md)
- [typealias CallHostBlock](./callhostblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdatasize64proc)*