# serviceIdentifier

**Framework**: Authentication Services  
**Kind**: property

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

## See Also

- [init(user: String, serviceIdentifier: ASCredentialServiceIdentifier, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/init(user:serviceidentifier:userinfo:).md)
  Creates a request to upgrade from using passwords to using Sign in with Apple.
- [var user: String](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/user.md)
  The user name of the account to upgrade.
- [var userInfo: [AnyHashable : Any]?](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/userinfo.md)
  A dictionary that contains values to pass to your account modification extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/serviceidentifier)*