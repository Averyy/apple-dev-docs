# accountAuthenticationModificationController(_:didSuccessfullyComplete:userInfo:)

**Framework**: Authentication Services  
**Kind**: method

Tells the delegate an account modification request completed successfully.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func accountAuthenticationModificationController(_ controller: ASAccountAuthenticationModificationController, didSuccessfullyComplete request: ASAccountAuthenticationModificationRequest, userInfo: [AnyHashable : Any]? = nil)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Parameters

- `controller`: The account authentication modification controller that initiated the request.
- `request`: The request that failed.
- `userInfo`: A dictionary that contains values from the account modification extension.

## See Also

- [func accountAuthenticationModificationController(ASAccountAuthenticationModificationController, didFail: ASAccountAuthenticationModificationRequest, error: any Error)](asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didfail:error:).md)
  Tells the delegate an account modification request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didsuccessfullycomplete:userinfo:))*