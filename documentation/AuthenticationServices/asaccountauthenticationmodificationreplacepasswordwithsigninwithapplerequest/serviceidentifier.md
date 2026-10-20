# serviceIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

An identifier that represents a particular service that the user needs a credential for, like a web site.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var serviceIdentifier: ASCredentialServiceIdentifier { get }
```

```objc
@property (nonatomic, readonly) ASCredentialServiceIdentifier * serviceIdentifier;
```

## See Also

### Creating Upgrade Requests in Your App
- [init(user: String, serviceIdentifier: ASCredentialServiceIdentifier, userInfo: [AnyHashable : Any]?)](./init%28user,serviceidentifier,userinfo%29.md)
  Creates a request to upgrade from using passwords to using Sign in with Apple.
- [var user: String](./user.md)
  The user name of the account to upgrade.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary that contains values to pass to your account modification extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/serviceidentifier)*