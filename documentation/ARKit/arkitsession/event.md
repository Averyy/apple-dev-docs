# ARKitSession.Event

**Framework**: ARKit  
**Kind**: enum

The kinds of events that can occur in a session.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
enum Event
```

## Topics

### Observing session events
- [case authorizationChanged(type: ARKitSession.AuthorizationType, status: ARKitSession.AuthorizationStatus)](arkitsession/event/authorizationchanged(type:status:).md)
  An event that represents a change in authorization status for a specific authorization type.
- [case dataProviderStateChanged(dataProviders: [any DataProvider], newState: DataProviderState, error: ARKitSession.Error?)](arkitsession/event/dataproviderstatechanged(dataproviders:newstate:error:).md)
  An event that represents a change in state of one of the data providers associated with a session.
### Instance Properties
- [var description: String](arkitsession/event/description.md)
  A textual representation of ARKitSession.Event

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var events: ARKitSession.Events](arkitsession/events-swift.property.md)
  An asynchronous sequence of events that provide updates to the current authorization status of the session.
- [ARKitSession.Events](arkitsession/events-swift.struct.md)
  A sequence of events.
- [var description: String](arkitsession/description.md)
  A textual representation of this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/event)*