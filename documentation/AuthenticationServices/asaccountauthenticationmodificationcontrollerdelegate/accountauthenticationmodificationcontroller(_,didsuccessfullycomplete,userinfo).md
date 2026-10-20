# accountAuthenticationModificationController(_:didSuccessfullyComplete:userInfo:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) accountAuthenticationModificationController:(ASAccountAuthenticationModificationController *) controller didSuccessfullyCompleteRequest:(ASAccountAuthenticationModificationRequest *) request withUserInfo:(NSDictionary *) userInfo;
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](../upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Parameters

- `controller`: The account authentication modification controller that initiated the request.
- `request`: The request that failed.
- `userInfo`: A dictionary that contains values from the account modification extension.

## See Also

### Handling Requests
- [func accountAuthenticationModificationController(ASAccountAuthenticationModificationController, didFail: ASAccountAuthenticationModificationRequest, error: any Error)](./accountauthenticationmodificationcontroller%28_,didfail,error%29.md)
  Tells the delegate an account modification request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didsuccessfullycomplete:userinfo:))*