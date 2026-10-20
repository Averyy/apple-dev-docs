# performRequests(options:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Starts the specified authorization flows during controller initialization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func performRequests(options: ASAuthorizationController.RequestOptions = [])
```

```objc
- (void) performRequestsWithOptions:(ASAuthorizationControllerRequestOptions) options;
```

## See Also

### Executing requests
- [func performRequests()](./performrequests%28%29.md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](./performautofillassistedrequests%28%29.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [func cancel()](./cancel%28%29.md)
  Cancels any active authorization requests.
- [ASAuthorizationController.RequestOptions](./requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/performrequests(options:))*