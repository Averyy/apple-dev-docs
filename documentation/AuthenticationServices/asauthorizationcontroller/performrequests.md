# performRequests()

**Framework**: Authentication Services  
**Kind**: method

Starts the specified authorization flows during controller initialization.

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
func performRequests()
```

## Mentions

- [Supporting passkeys](supporting-passkeys.md)
- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)

#### Discussion

When authorization succeeds, the system relays that information to the controller’s [`delegate`](asauthorizationcontroller/delegate.md) by calling the [`authorizationController(controller:didCompleteWithAuthorization:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md) method with an authorization instance. If authorization fails, the system calls the [`authorizationController(controller:didCompleteWithError:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:).md) method instead.

Some authorization flows require a presentation context to ask the user for information or consent. Adopt the `ASAuthorizationControllerPresenting` protocol in one of your app’s classes, and set an instance of that class as the authorization controller’s `presentationController`.

## See Also

- [func performRequests(options: ASAuthorizationController.RequestOptions)](asauthorizationcontroller/performrequests(options:).md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](asauthorizationcontroller/performautofillassistedrequests.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [func cancel()](asauthorizationcontroller/cancel.md)
  Cancels any active authorization requests.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/performrequests())*