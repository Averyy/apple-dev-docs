# accountAuthenticationModificationController(_:didFail:error:)

**Framework**: Authentication Services  
**Kind**: method

Tells the delegate an account modification request failed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func accountAuthenticationModificationController(_ controller: ASAccountAuthenticationModificationController, didFail request: ASAccountAuthenticationModificationRequest, error: any Error)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Parameters

- `controller`: The account authentication modification controller that initiated the request.
- `request`: The request that failed.
- `error`: An error that indicates why the request failed.

## See Also

- [func accountAuthenticationModificationController(ASAccountAuthenticationModificationController, didSuccessfullyComplete: ASAccountAuthenticationModificationRequest, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didsuccessfullycomplete:userinfo:).md)
  Tells the delegate an account modification request completed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didfail:error:))*