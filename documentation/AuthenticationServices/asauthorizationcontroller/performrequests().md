# performRequests()

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) performRequests;
```

## Mentions

- [Authenticating people by using passkeys in browser apps](../authenticating-people-by-using-passkeys-in-browser-apps.md)
- [Supporting passkeys](../supporting-passkeys.md)

#### Discussion

When authorization succeeds, the system relays that information to the controller’s [`delegate`](./delegate.md) by calling the [`authorizationController(controller:didCompleteWithAuthorization:)`](../asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewithauthorization%29.md) method with an authorization instance. If authorization fails, the system calls the [`authorizationController(controller:didCompleteWithError:)`](../asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewitherror%29.md) method instead.

Some authorization flows require a presentation context to ask the user for information or consent. Adopt the `ASAuthorizationControllerPresenting` protocol in one of your app’s classes, and set an instance of that class as the authorization controller’s `presentationController`.

## See Also

### Executing requests
- [func performRequests(options: ASAuthorizationController.RequestOptions)](./performrequests%28options%29.md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](./performautofillassistedrequests%28%29.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [func cancel()](./cancel%28%29.md)
  Cancels any active authorization requests.
- [ASAuthorizationController.RequestOptions](./requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/performrequests())*