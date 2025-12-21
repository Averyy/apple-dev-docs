# performAutoFillAssistedRequests()

**Framework**: Authentication Services  
**Kind**: method

Initiates the authorization flows for requests that support AutoFill presentation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func performAutoFillAssistedRequests()
```

## Mentions

- [Authenticating people by using passkeys in browser apps](authenticating-people-by-using-passkeys-in-browser-apps.md)
- [Supporting passkeys](supporting-passkeys.md)

#### Discussion

The authorization controller presents a user interface when a text field with the appropriate text content type obtains focus.

Upon completion, the authorization controller calls its delegate to report success or failure.

## See Also

- [func performRequests()](asauthorizationcontroller/performrequests.md)
  Starts the specified authorization flows during controller initialization.
- [func performRequests(options: ASAuthorizationController.RequestOptions)](asauthorizationcontroller/performrequests(options:).md)
  Starts the specified authorization flows during controller initialization.
- [func cancel()](asauthorizationcontroller/cancel.md)
  Cancels any active authorization requests.
- [ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions.md)
  Options that modify how a controller performs authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/performautofillassistedrequests())*