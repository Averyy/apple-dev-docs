# CAClockAddListener(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockAddListener(_ inCAClock: CAClockRef, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus CAClockAddListener(CAClockRef inCAClock, CAClockListenerProc inListenerProc, void *inUserData);
```

## See Also

### Adding and Removing Listeners
- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockremovelistener%28_,_,_%29.md)
- [typealias CAClockListenerProc](./caclocklistenerproc.md)
- [enum CAClockMessage](./caclockmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockaddlistener(_:_:_:))*