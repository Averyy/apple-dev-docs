# ARKitSession.Event.dataProviderStateChanged(dataProviders:newState:error:)

**Framework**: ARKit  
**Kind**: case

An event that represents a change in state of one of the data providers associated with a session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
case dataProviderStateChanged(dataProviders: [any DataProvider], newState: DataProviderState, error: ARKitSession.Error?)
```

## Parameters

- `dataProviders`: The data providers associated with this session.
- `newState`: The state that changed to cause the event.
- `error`: A session error assocated with the state change.

## See Also

- [case authorizationChanged(type: ARKitSession.AuthorizationType, status: ARKitSession.AuthorizationStatus)](arkitsession/event/authorizationchanged(type:status:).md)
  An event that represents a change in authorization status for a specific authorization type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/event/dataproviderstatechanged(dataproviders:newstate:error:))*