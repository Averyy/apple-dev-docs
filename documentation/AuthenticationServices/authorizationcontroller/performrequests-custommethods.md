# performRequests(_:customMethods:)

**Framework**: Authentication Services  
**Kind**: method

Performs an authorization request from the provided array using a custom authorization method.

**Availability**:
- tvOS 16.4+

## Declaration

```swift
@MainActor
func performRequests(_ requests: [ASAuthorizationRequest], customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult
```

#### Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](asauthorizationresult.md).

#### Discussion

The framework checks each authorization request in the array against the credentials available on the person’s device; the more credential types your app supports, the more options a person can choose from.

If the return value is [`ASAuthorizationResult.customMethod(_:)`](asauthorizationresult/custommethod(_:).md), use the case’s associated value to access the chosen authorization method.

## Parameters

- `requests`: An array of supported authorization requests.
- `customMethods`: An array of custom authorization methods to display in the system authorization UI. For more information, see  .

## See Also

- [func performRequest(ASAuthorizationRequest) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:).md)
  Performs the specified authorization request.
- [func performRequests([ASAuthorizationRequest]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:).md)
  Performs an authorization request from the provided array.
- [func performRequest(ASAuthorizationRequest, options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:options:).md)
  Performs the specified authorization request with explicit options.
- [func performRequests([ASAuthorizationRequest], options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:options:).md)
  Performs an authorization request, with explicit options, from the provided array.
- [func performRequest(ASAuthorizationRequest, customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:custommethods:).md)
  Performs the authorization request using a custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performrequests(_:custommethods:))*