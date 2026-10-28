# skipped

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

An event that takes place when the system misses an action event’s time interval.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static var skipped: ActionEventType { get }
```

## Discussion

RealityKit generates a skip event under the following conditions:

- The current time is greater than or equal to the event’s ending time.
- The previous frame’s time is less than the event’s starting time.

## See Also

### Event types
- [static var started: ActionEventType](./started.md)
  An event that takes place when a new action event begins.
- [static var ended: ActionEventType](./ended.md)
  An event that takes place when the action event exits its time interval.
- [static var paused: ActionEventType](./paused.md)
  An event that takes place when the animation pauses.
- [static var resumed: ActionEventType](./resumed.md)
  An event that takes place when the animation resumes after a pause.
- [static var updated: ActionEventType](./updated.md)
  An event that takes place after an action event starts and is within its time interval.
- [static var terminated: ActionEventType](./terminated.md)
  An event that takes place when the animation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventtype/skipped)*