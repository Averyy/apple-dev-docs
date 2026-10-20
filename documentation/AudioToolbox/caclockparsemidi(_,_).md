# CAClockParseMIDI(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CAClockParseMIDI(_ inCAClock: CAClockRef, _ inMIDIPacketList: UnsafePointer<MIDIPacketList>) -> OSStatus
```

```c
extern OSStatus CAClockParseMIDI(CAClockRef inCAClock, const struct MIDIPacketList *inMIDIPacketList);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockparsemidi(_:_:))*