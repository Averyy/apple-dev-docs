# cancel()

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancel;
```

## Discussion

If calling this method cancels an active authorization request, the authorization controller calls its delegate’s [`authorizationController(controller:didCompleteWithError:)`](../asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewitherror%29.md) method.

## See Also

### Executing requests
- [func performRequests()](./performrequests%28%29.md)
  Starts the specified authorization flows during controller initialization.
- [func performRequests(options: ASAuthorizationController.RequestOptions)](./performrequests%28options%29.md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](./performautofillassistedrequests%28%29.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [ASAuthorizationController.RequestOptions](./requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/cancel())*