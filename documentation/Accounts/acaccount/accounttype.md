# accountType

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

The type of service account.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
var accountType: ACAccountType! { get set }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, strong) ACAccountType * accountType;
```

*macOS*

```objc
@property (atomic, strong) ACAccountType * accountType;
```

#### Discussion

This property is required. You specify the account type using the [`init(accountType:)`](./init%28accounttype%29.md) method. You can use the [`accounts(with:)`](../acaccountstore/accounts%28with%29.md) method to retrieve all accounts of a particular type.

## See Also

### Accessing Properties
- [var accountDescription: String!](./accountdescription.md)
  A human-readable description of the account.
- [var credential: ACAccountCredential!](./credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](./identifier.md)
  A unique identifier for this account.
- [var username: String!](./username.md)
  The username for this account.
- [var userFullName: String!](./userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/accounttype)*