# userInfo

**Framework**: Authentication Services  
**Kind**: property

A dictionary that contains values to pass to your account modification extension.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

## See Also

- [init(user: String, serviceIdentifier: ASCredentialServiceIdentifier, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/init(user:serviceidentifier:userinfo:).md)
  Creates a request to upgrade from using a weak password to using a strong system-generated password.
- [var user: String](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/user.md)
  The user name of the account to upgrade.
- [var serviceIdentifier: ASCredentialServiceIdentifier](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/serviceidentifier.md)
  An identifier that represents a particular service that the user needs a credential for, like a web site.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/userinfo)*