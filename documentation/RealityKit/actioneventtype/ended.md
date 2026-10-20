# ended

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

An event that takes place when the action event exits its time interval.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static var ended: ActionEventType { get }
```

#### Discussion

End is also raised when the animation terminates before the action event completes.

## See Also

### Event types
- [static var started: ActionEventType](./started.md)
  An event that takes place when a new action event begins.
- [static var paused: ActionEventType](./paused.md)
  An event that takes place when the animation pauses.
- [static var resumed: ActionEventType](./resumed.md)
  An event that takes place when the animation resumes after a pause.
- [static var updated: ActionEventType](./updated.md)
  An event that takes place after an action event starts and is within its time interval.
- [static var skipped: ActionEventType](./skipped.md)
  An event that takes place when the system misses an action event’s time interval.
- [static var terminated: ActionEventType](./terminated.md)
  An event that takes place when the animation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventtype/ended)*