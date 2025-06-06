# init(user:serviceIdentifier:userInfo:)

**Framework**: Authentication Services  
**Kind**: init

Creates a request to upgrade from using passwords to using Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
init(user: String, serviceIdentifier: ASCredentialServiceIdentifier, userInfo: [AnyHashable : Any]? = nil)
```

#### Return Value

An initialized request object with details about the account to upgrade to Sign in with Apple.

#### Discussion

If your extension needs information to authenticate with your server, such as an authentication token, set it in the `userInfo` dictionary before calling this method.

## Parameters

- `user`: The user name of the account to upgrade.
- `serviceIdentifier`: An identifier that represents a particular service that the user needs a credential for, like a web site.
- `userInfo`: A dictionary that contains values to pass to your account modification extension.

## See Also

- [var user: String](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/user.md)
  The user name of the account to upgrade.
- [var serviceIdentifier: ASCredentialServiceIdentifier](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/serviceidentifier.md)
  An identifier that represents a particular service that the user needs a credential for, like a web site.
- [var userInfo: [AnyHashable : Any]?](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/userinfo.md)
  A dictionary that contains values to pass to your account modification extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest/init(user:serviceidentifier:userinfo:))*