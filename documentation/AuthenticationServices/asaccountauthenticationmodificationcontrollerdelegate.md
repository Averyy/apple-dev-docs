# ASAccountAuthenticationModificationControllerDelegate

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface you implement for receiving success and failure statuses about modification of an account’s authentication properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASAccountAuthenticationModificationControllerDelegate : NSObjectProtocol
```

```objc
@protocol ASAccountAuthenticationModificationControllerDelegate <NSObject>
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](./upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Topics

### Handling Requests
- [func accountAuthenticationModificationController(ASAccountAuthenticationModificationController, didSuccessfullyComplete: ASAccountAuthenticationModificationRequest, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller%28_,didsuccessfullycomplete,userinfo%29.md)
  Tells the delegate an account modification request completed successfully.
- [func accountAuthenticationModificationController(ASAccountAuthenticationModificationController, didFail: ASAccountAuthenticationModificationRequest, error: any Error)](./asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller%28_,didfail,error%29.md)
  Tells the delegate an account modification request failed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling Modification Requests
- [func cancelRequest()](./asaccountauthenticationmodificationviewcontroller/cancelrequest%28%29.md)
  Cancels a request that the user initiated.
- [protocol ASAccountAuthenticationModificationControllerPresentationContextProviding](./asaccountauthenticationmodificationcontrollerpresentationcontextproviding.md)
  An interface you implement to coordinate presentation of the user interface when modifying an account’s authentication properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontrollerdelegate)*