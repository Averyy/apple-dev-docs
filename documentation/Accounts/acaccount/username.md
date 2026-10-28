# username

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

The username for this account.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
var username: String! { get set }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, copy) NSString * username;
```

*macOS*

```objc
@property (atomic, copy) NSString * username;
```

## Discussion

This property must be set before the account is saved. After the account is saved, this property is available if the user grants the application access to this account; otherwise it’s `nil`.

## See Also

### Accessing Properties
- [var accountDescription: String!](./accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](./accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](./credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](./identifier.md)
  A unique identifier for this account.
- [var userFullName: String!](./userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/username)*