# queryAuthorization(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Checks whether the current session is authorized for particular authorization types without requesting authorization.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final func queryAuthorization(for authorizationTypes: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]
```

## Return Value

A list of the authorization statuses for each authorization type you passed in `authorizationTypes`.

## Parameters

- `authorizationTypes`: The authorization types you want to check.

## See Also

### Getting authorization
- [func requestAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](./requestauthorization%28for%29.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ARKitSession.AuthorizationType](./authorizationtype.md)
  The authorization types you can request from ARKit.
- [ARKitSession.AuthorizationStatus](./authorizationstatus.md)
  The authorization states for a type of ARKit data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/queryauthorization(for:))*