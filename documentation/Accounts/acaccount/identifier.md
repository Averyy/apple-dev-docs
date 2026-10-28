# identifier

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

A unique identifier for this account.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
weak var identifier: NSString! { get }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, weak, readonly) NSString * identifier;
```

*macOS*

```objc
@property (atomic, weak, readonly) NSString * identifier;
```

## Discussion

Use the [`account(withIdentifier:)`](../acaccountstore/account%28withidentifier%29.md) method to get an account with the specified identifier.

## See Also

### Accessing Properties
- [var accountDescription: String!](./accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](./accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](./credential.md)
  The credential used to authenticate the user of this account.
- [var username: String!](./username.md)
  The username for this account.
- [var userFullName: String!](./userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/identifier)*