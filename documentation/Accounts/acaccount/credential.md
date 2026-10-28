# credential

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

The credential used to authenticate the user of this account.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
var credential: ACAccountCredential! { get set }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, strong) ACAccountCredential * credential;
```

*macOS*

```objc
@property (atomic, strong) ACAccountCredential * credential;
```

## Discussion

This property is required and must be set before the account is saved. For privacy reasons, this property is inaccessible after the account is saved.

## See Also

### Accessing Properties
- [var accountDescription: String!](./accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](./accounttype.md)
  The type of service account.
- [var identifier: NSString!](./identifier.md)
  A unique identifier for this account.
- [var username: String!](./username.md)
  The username for this account.
- [var userFullName: String!](./userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/credential)*