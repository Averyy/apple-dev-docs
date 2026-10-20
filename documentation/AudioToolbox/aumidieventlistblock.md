# AUMIDIEventListBlock

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AUMIDIEventListBlock = (AUEventSampleTime, UInt8, UnsafePointer<MIDIEventList>) -> OSStatus
```

```c
typedef int (^)(long long, unsigned char, const struct MIDIEventList *) __attribute__((nonblocking)) AUMIDIEventListBlock;
```

## See Also

### Data Types
- [typealias AudioFileComponentGetUserDataAtOffsetProc](./audiofilecomponentgetuserdataatoffsetproc.md)
- [typealias AudioFileComponentGetUserDataSize64Proc](./audiofilecomponentgetuserdatasize64proc.md)
- [typealias CallHostBlock](./callhostblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumidieventlistblock)*