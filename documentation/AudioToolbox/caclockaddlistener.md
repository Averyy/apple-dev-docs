# CAClockAddListener(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockAddListener(_ inCAClock: CAClockRef, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](caclockremovelistener(_:_:_:).md)
- [typealias CAClockListenerProc](caclocklistenerproc.md)
- [enum CAClockMessage](caclockmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockaddlistener(_:_:_:))*