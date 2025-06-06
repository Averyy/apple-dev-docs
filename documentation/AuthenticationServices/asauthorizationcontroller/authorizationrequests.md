# authorizationRequests

**Framework**: Authentication Services  
**Kind**: property

The authorization requests that the controller manages.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var authorizationRequests: [ASAuthorizationRequest] { get }
```

#### Discussion

Use an authorization provider, like [`ASAuthorizationAppleIDProvider`](asauthorizationappleidprovider.md), [`ASAuthorizationPasswordProvider`](asauthorizationpasswordprovider.md), or [`ASAuthorizationSingleSignOnProvider`](asauthorizationsinglesignonprovider.md), to create a request for a particular purpose.

## See Also

- [class ASAuthorizationRequest](asauthorizationrequest.md)
  A base class for different kinds of authorization requests.
- [var customAuthorizationMethods: [ASAuthorizationCustomMethod]](asauthorizationcontroller/customauthorizationmethods.md)
  An array of custom authorization methods for the user to choose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/authorizationrequests)*