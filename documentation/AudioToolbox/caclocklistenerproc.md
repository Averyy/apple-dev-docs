# CAClockListenerProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias CAClockListenerProc = (UnsafeMutableRawPointer, CAClockMessage, UnsafeRawPointer) -> Void
```

```c
typedef void (*)(void *, enum CAClockMessage, const void *) CAClockListenerProc;
```

## See Also

### Adding and Removing Listeners
- [func CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockaddlistener%28_,_,_%29.md)
- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockremovelistener%28_,_,_%29.md)
- [enum CAClockMessage](./caclockmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocklistenerproc)*