# performRequest(_:customMethods:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Performs the authorization request using a custom authorization method.

**Availability**:
- tvOS 16.4+

## Declaration

```swift
@MainActor
func performRequest(_ request: ASAuthorizationRequest, customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult
```

## Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](../asauthorizationresult.md).

## Discussion

If the return value is [`ASAuthorizationResult.customMethod(_:)`](../asauthorizationresult/custommethod%28_%29.md), use the case’s associated value to access the chosen authorization method.

## Parameters

- `request`: The authorization request to perform.
- `customMethods`: An array of custom authorization methods to display in the system authorization UI. For more information, see [`ASAuthorizationCustomMethod`](../asauthorizationcustommethod.md).

## See Also

### Performing requests
- [func performRequest(ASAuthorizationRequest) async throws -> ASAuthorizationResult](./performrequest%28_%29.md)
  Performs the specified authorization request.
- [func performRequests([ASAuthorizationRequest]) async throws -> ASAuthorizationResult](./performrequests%28_%29.md)
  Performs an authorization request from the provided array.
- [func performRequest(ASAuthorizationRequest, options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](./performrequest%28_,options%29.md)
  Performs the specified authorization request with explicit options.
- [func performRequests([ASAuthorizationRequest], options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](./performrequests%28_,options%29.md)
  Performs an authorization request, with explicit options, from the provided array.
- [func performRequests([ASAuthorizationRequest], customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](./performrequests%28_,custommethods%29.md)
  Performs an authorization request from the provided array using a custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performrequest(_:custommethods:))*