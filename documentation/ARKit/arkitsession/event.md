# ARKitSession.Event

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration of possible session events.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum Event
```

## Topics

### Enumeration Cases
- [case authorizationChanged(type: ARKitSession.AuthorizationType, status: ARKitSession.AuthorizationStatus)](./event/authorizationchanged%28type,status%29.md)
  An event that represents a change in authorization status for a specific authorization type.
- [case dataProviderStateChanged(dataProviders: [any DataProvider], newState: DataProviderState, error: ARKitSession.Error?)](./event/dataproviderstatechanged%28dataproviders,newstate,error%29.md)
  An event that represents a state change of one or more of the data providers associated with a session.
### Instance Properties
- [var description: String](./event/description.md)
  A textual representation of ARKitSession.Event

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing a session
- [var events: ARKitSession.Events](./events-swift.property.md)
  An asynchronous sequence of events that describe changes to the session, such as authorization changes and data-provider state changes.
- [ARKitSession.Events](./events-swift.struct.md)
  A sequence of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/event)*