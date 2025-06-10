# ARKitSession.AuthorizationStatus

**Framework**: ARKit  
**Kind**: enum

The authorization states for a type of ARKit data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum AuthorizationStatus
```

## Topics

### Getting authorization states
- [ARKitSession.AuthorizationStatus.notDetermined](arkitsession/authorizationstatus/notdetermined.md)
  The user hasn’t yet granted or denied permission.
- [ARKitSession.AuthorizationStatus.allowed](arkitsession/authorizationstatus/allowed.md)
  The user granted your app permission to use the associated kind of ARKit data.
- [ARKitSession.AuthorizationStatus.denied](arkitsession/authorizationstatus/denied.md)
  The user denied your app permission to use the associated kind of ARKit data.
### Instance Properties
- [var description: String](arkitsession/authorizationstatus/description.md)
  A textual representation of AuthorizationStatus

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/requestauthorization(for:).md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ARKitSession.AuthorizationType](arkitsession/authorizationtype.md)
  The authorization types you can request from ARKit.
- [func queryAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/queryauthorization(for:).md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/authorizationstatus)*