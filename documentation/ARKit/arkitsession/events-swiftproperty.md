# events

**Framework**: ARKit  
**Kind**: property

An asynchronous sequence of events that provide updates to the current authorization status of the session.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
final var events: ARKitSession.Events { get }
```

#### Discussion

The following example detects changes in the current session’s authorization status.

```swift
let session = ARKitSession()
Task {
    for await update in session.events {
        if case .authorizationChanged(let type, let status) = update {
            print("Authorization. Status of \(type) changed to \(status).")
        } else {
            print("Another session event \(update).")
        }
    }
}
```

## See Also

- [ARKitSession.Events](arkitsession/events-swift.struct.md)
  A sequence of events.
- [ARKitSession.Event](arkitsession/event.md)
  The kinds of events that can occur in a session.
- [var description: String](arkitsession/description.md)
  A textual representation of this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.property)*