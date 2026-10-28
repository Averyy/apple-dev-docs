# performRequest(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Performs the specified authorization request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
@MainActor
func performRequest(_ request: ASAuthorizationRequest) async throws -> ASAuthorizationResult
```

## Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](../asauthorizationresult.md).

## Parameters

- `request`: The authorization request to perform.

## See Also

### Performing requests
- [func performRequests([ASAuthorizationRequest]) async throws -> ASAuthorizationResult](./performrequests%28_%29.md)
  Performs an authorization request from the provided array.
- [func performRequest(ASAuthorizationRequest, options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](./performrequest%28_,options%29.md)
  Performs the specified authorization request with explicit options.
- [func performRequests([ASAuthorizationRequest], options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](./performrequests%28_,options%29.md)
  Performs an authorization request, with explicit options, from the provided array.
- [func performRequest(ASAuthorizationRequest, customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](./performrequest%28_,custommethods%29.md)
  Performs the authorization request using a custom authorization method.
- [func performRequests([ASAuthorizationRequest], customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](./performrequests%28_,custommethods%29.md)
  Performs an authorization request from the provided array using a custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performrequest(_:))*