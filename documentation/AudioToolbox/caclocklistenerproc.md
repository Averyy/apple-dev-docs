# CAClockListenerProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias CAClockListenerProc = (UnsafeMutableRawPointer, CAClockMessage, UnsafeRawPointer) -> Void
```

## See Also

- [func CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](caclockaddlistener(_:_:_:).md)
- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](caclockremovelistener(_:_:_:).md)
- [enum CAClockMessage](caclockmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocklistenerproc)*