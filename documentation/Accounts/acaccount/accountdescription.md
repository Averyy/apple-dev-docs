# accountDescription

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

A human-readable description of the account.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
var accountDescription: String! { get set }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, copy) NSString * accountDescription;
```

*macOS*

```objc
@property (atomic, copy) NSString * accountDescription;
```

## Discussion

This property is available if the user grants the application access to this account; otherwise it’s `nil`.

## See Also

### Accessing Properties
- [var accountType: ACAccountType!](./accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](./credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](./identifier.md)
  A unique identifier for this account.
- [var username: String!](./username.md)
  The username for this account.
- [var userFullName: String!](./userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/accountdescription)*