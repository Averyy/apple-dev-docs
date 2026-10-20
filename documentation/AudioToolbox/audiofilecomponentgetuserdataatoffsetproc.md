# AudioFileComponentGetUserDataAtOffsetProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentGetUserDataAtOffsetProc = (UnsafeMutableRawPointer, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, long long, unsigned int *, void *) AudioFileComponentGetUserDataAtOffsetProc;
```

## See Also

### Data Types
- [typealias AUMIDIEventListBlock](./aumidieventlistblock.md)
- [typealias AudioFileComponentGetUserDataSize64Proc](./audiofilecomponentgetuserdatasize64proc.md)
- [typealias CallHostBlock](./callhostblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdataatoffsetproc)*