# ARKitSession.AuthorizationStatus

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The authorization states for a type of ARKit data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum AuthorizationStatus
```

## Topics

### Getting authorization states
- [ARKitSession.AuthorizationStatus.notDetermined](./authorizationstatus/notdetermined.md)
  The user hasn’t yet granted or denied permission.
- [ARKitSession.AuthorizationStatus.allowed](./authorizationstatus/allowed.md)
  The user granted your app permission to use the associated kind of ARKit data.
- [ARKitSession.AuthorizationStatus.denied](./authorizationstatus/denied.md)
  The user denied your app permission to use the associated kind of ARKit data.
### Instance Properties
- [var description: String](./authorizationstatus/description.md)
  A textual representation of AuthorizationStatus

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting authorization
- [func requestAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](./requestauthorization%28for%29.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ARKitSession.AuthorizationType](./authorizationtype.md)
  The authorization types you can request from ARKit.
- [func queryAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](./queryauthorization%28for%29.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/authorizationstatus)*