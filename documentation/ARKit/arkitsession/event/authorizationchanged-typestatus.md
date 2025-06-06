# ARKitSession.Event.authorizationChanged(type:status:)

**Framework**: ARKit  
**Kind**: case

An event that represents a change in authorization status for a specific authorization type.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
case authorizationChanged(type: ARKitSession.AuthorizationType, status: ARKitSession.AuthorizationStatus)
```

## Parameters

- `type`: The type of authorization status that changed.
- `status`: The new state of authorization.

## See Also

- [case dataProviderStateChanged(dataProviders: [any DataProvider], newState: DataProviderState, error: ARKitSession.Error?)](arkitsession/event/dataproviderstatechanged(dataproviders:newstate:error:).md)
  An event that represents a change in state of one of the data providers associated with a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/event/authorizationchanged(type:status:))*