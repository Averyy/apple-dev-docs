# performRequest(_:options:)

**Framework**: Authentication Services  
**Kind**: method

Performs the specified authorization request with explicit options.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performRequest(_ request: ASAuthorizationRequest, options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult
```

#### Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](asauthorizationresult.md).

## Parameters

- `request`: The authorization request to perform.
- `options`: Additional options that customize the request’s behavior. For more information, see  .

## See Also

- [func performRequest(ASAuthorizationRequest) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:).md)
  Performs the specified authorization request.
- [func performRequests([ASAuthorizationRequest]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:).md)
  Performs an authorization request from the provided array.
- [func performRequests([ASAuthorizationRequest], options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:options:).md)
  Performs an authorization request, with explicit options, from the provided array.
- [func performRequest(ASAuthorizationRequest, customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:custommethods:).md)
  Performs the authorization request using a custom authorization method.
- [func performRequests([ASAuthorizationRequest], customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:custommethods:).md)
  Performs an authorization request from the provided array using a custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performrequest(_:options:))*