# stationary

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An event phase is in progress but hasn’t moved since the previous event.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var stationary: NSEvent.Phase { get }
```

```c
NSEventPhaseStationary
```

## See Also

### Constants
- [static var began: NSEvent.Phase](./began.md)
  An event phase has begun.
- [static var changed: NSEvent.Phase](./changed.md)
  An event phase has changed.
- [static var ended: NSEvent.Phase](./ended.md)
  The event phase ended.
- [static var cancelled: NSEvent.Phase](./cancelled.md)
  The system canceled the event phase.
- [static var mayBegin: NSEvent.Phase](./maybegin.md)
  The system event phase may begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/phase-swift.struct/stationary)*