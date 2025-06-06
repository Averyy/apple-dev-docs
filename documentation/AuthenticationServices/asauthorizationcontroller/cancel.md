# cancel()

**Framework**: Authentication Services  
**Kind**: method

Cancels any active authorization requests.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

#### Discussion

If calling this method cancels an active authorization request, the authorization controller calls its delegate’s [`authorizationController(controller:didCompleteWithError:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:).md) method.

## See Also

- [func performRequests()](asauthorizationcontroller/performrequests.md)
  Starts the specified authorization flows during controller initialization.
- [func performRequests(options: ASAuthorizationController.RequestOptions)](asauthorizationcontroller/performrequests(options:).md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](asauthorizationcontroller/performautofillassistedrequests.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/cancel())*