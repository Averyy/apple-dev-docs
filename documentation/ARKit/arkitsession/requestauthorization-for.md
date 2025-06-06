# requestAuthorization(for:)

**Framework**: ARKit  
**Kind**: method

Requests authorization from the user to use the specified kinds of ARKit data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final func requestAuthorization(for authorizationTypes: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]
```

#### Return Value

A dictionary that contains the result of the authorization request for each authorization type you requested.

#### Discussion

You can use the [`requiredAuthorizations`](dataprovider/requiredauthorizations.md) property on any of the types that conform to the [`DataProvider`](dataprovider.md) protocol to get the list of authorizations specific to that data provider and pass it to this method.

## Parameters

- `authorizationTypes`: The types of authorizations your app needs to run.

## See Also

- [ARKitSession.AuthorizationType](arkitsession/authorizationtype.md)
  The authorization types you can request from ARKit.
- [func queryAuthorization(for: [ARKitSession.AuthorizationType]) async -> [ARKitSession.AuthorizationType : ARKitSession.AuthorizationStatus]](arkitsession/queryauthorization(for:).md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ARKitSession.AuthorizationStatus](arkitsession/authorizationstatus.md)
  The authorization states for a type of ARKit data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/requestauthorization(for:))*