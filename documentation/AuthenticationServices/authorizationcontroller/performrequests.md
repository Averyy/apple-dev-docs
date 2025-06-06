# performRequests(_:)

**Framework**: Authentication Services  
**Kind**: method

Performs an authorization request from the provided array.

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
func performRequests(_ requests: [ASAuthorizationRequest]) async throws -> ASAuthorizationResult
```

#### Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](asauthorizationresult.md).

#### Discussion

The framework checks each authorization request in the array against the credentials available on the person’s device; the more credential types your app supports, the more options a person can choose from.

## Parameters

- `requests`: An array of supported authorization requests.

## See Also

- [func performRequest(ASAuthorizationRequest) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:).md)
  Performs the specified authorization request.
- [func performRequest(ASAuthorizationRequest, options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:options:).md)
  Performs the specified authorization request with explicit options.
- [func performRequests([ASAuthorizationRequest], options: ASAuthorizationController.RequestOptions) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:options:).md)
  Performs an authorization request, with explicit options, from the provided array.
- [func performRequest(ASAuthorizationRequest, customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequest(_:custommethods:).md)
  Performs the authorization request using a custom authorization method.
- [func performRequests([ASAuthorizationRequest], customMethods: [ASAuthorizationCustomMethod]) async throws -> ASAuthorizationResult](authorizationcontroller/performrequests(_:custommethods:).md)
  Performs an authorization request from the provided array using a custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performrequests(_:))*