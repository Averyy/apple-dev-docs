# ASAuthorizationController

**Framework**: Authentication Services  
**Kind**: class

A controller that manages authorization requests that a provider creates.

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
class ASAuthorizationController
```

## Mentions

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

#### Overview

Create authorization requests for the credential types your app supports, such as [`ASAuthorizationAppleIDRequest`](asauthorizationappleidrequest.md) for Sign in with Apple, or [`ASAuthorizationPasswordRequest`](asauthorizationpasswordrequest.md) for password credentials. Create an authorization controller using [`init(authorizationRequests:)`](asauthorizationcontroller/init(authorizationrequests:).md), supplying the authorization requests you create. Set the authorization controller’s [`delegate`](asauthorizationcontroller/delegate.md) to receive responses when requests succeed or fail, and set its [`presentationContextProvider`](asauthorizationcontroller/presentationcontextprovider.md) so that the authorization controller can present UI.

Call [`performAutoFillAssistedRequests()`](asauthorizationcontroller/performautofillassistedrequests().md) to present inline UI to request credentials, or [`performRequests()`](asauthorizationcontroller/performrequests().md) or [`performRequests(options:)`](asauthorizationcontroller/performrequests(options:).md) to request credentials using modal UI. [`ASAuthorizationController`](asauthorizationcontroller.md) calls your delegate’s methods when the request completes.

Set the content type of text fields in your app’s login UI so that [`ASAuthorizationController`](asauthorizationcontroller.md) can detect when to offer AutoFill suggestions. Use [`username`](https://developer.apple.com/documentation/UIKit/UITextContentType/username) as the content type for user name text fields, and [`password`](https://developer.apple.com/documentation/UIKit/UITextContentType/password) for password fields.

## Topics

### Creating a controller
- [init(authorizationRequests: [ASAuthorizationRequest])](asauthorizationcontroller/init(authorizationrequests:).md)
  Creates a controller from a collection of authorization requests.
### Inspecting requests
- [class ASAuthorizationRequest](asauthorizationrequest.md)
  A base class for different kinds of authorization requests.
- [var authorizationRequests: [ASAuthorizationRequest]](asauthorizationcontroller/authorizationrequests.md)
  The authorization requests that the controller manages.
- [var customAuthorizationMethods: [ASAuthorizationCustomMethod]](asauthorizationcontroller/customauthorizationmethods.md)
  An array of custom authorization methods for the user to choose.
### Presenting requests
- [var presentationContextProvider: (any ASAuthorizationControllerPresentationContextProviding)?](asauthorizationcontroller/presentationcontextprovider.md)
  A delegate that provides a display context in which the system can present an authorization interface to the user.
- [protocol ASAuthorizationControllerPresentationContextProviding](asauthorizationcontrollerpresentationcontextproviding.md)
  An interface the controller uses to ask a delegate for a presentation context.
### Executing requests
- [func performRequests()](asauthorizationcontroller/performrequests.md)
  Starts the specified authorization flows during controller initialization.
- [func performRequests(options: ASAuthorizationController.RequestOptions)](asauthorizationcontroller/performrequests(options:).md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](asauthorizationcontroller/performautofillassistedrequests.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [func cancel()](asauthorizationcontroller/cancel.md)
  Cancels any active authorization requests.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.
### Responding to request completion
- [var delegate: (any ASAuthorizationControllerDelegate)?](asauthorizationcontroller/delegate.md)
  A delegate that the authorization controller informs about the success or failure of an authorization attempt.
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [protocol ASAuthorizationControllerDelegate](asauthorizationcontrollerdelegate.md)
  An interface for providing information about the outcome of an authorization request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct AuthorizationController](authorizationcontroller.md)
  A SwiftUI environment value that views use to perform authorization requests.
- [enum ASAuthorizationResult](asauthorizationresult.md)
  Describes the outcome of a successful authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller)*