# events

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence of events that describe changes to the session, such as authorization changes and data-provider state changes.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
final var events: ARKitSession.Events { get }
```

## Discussion

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

### Observing a session
- [ARKitSession.Events](./events-swift.struct.md)
  A sequence of events.
- [ARKitSession.Event](./event.md)
  Enumeration of possible session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.property)*