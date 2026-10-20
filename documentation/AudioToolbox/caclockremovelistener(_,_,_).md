# CAClockRemoveListener(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockRemoveListener(_ inCAClock: CAClockRef, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus CAClockRemoveListener(CAClockRef inCAClock, CAClockListenerProc inListenerProc, void *inUserData);
```

## See Also

### Adding and Removing Listeners
- [func CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockaddlistener%28_,_,_%29.md)
- [typealias CAClockListenerProc](./caclocklistenerproc.md)
- [enum CAClockMessage](./caclockmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockremovelistener(_:_:_:))*