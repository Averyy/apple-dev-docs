# presentAuthorizationViewController(completion:)

**Framework**: Authentication Services  
**Kind**: method

Asks the authorization service to show the extension’s view controller to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func presentAuthorizationViewController() async throws
```

#### Discussion

This is only valid during authentication requests. If the system can’t show the controller, the completion returns an error.

## Parameters

- `completion`: A completion handler that the method uses to indicate whether the view controller was presented successfully, and the specific error if not.

## See Also

- [var isUserInterfaceEnabled: Bool](asauthorizationproviderextensionauthorizationrequest/isuserinterfaceenabled.md)
  Determines if user interface is available for the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/presentauthorizationviewcontroller(completion:))*