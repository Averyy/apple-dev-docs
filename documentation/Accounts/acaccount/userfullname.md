# userFullName

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

The full name associated with the user account.

**Availability**:
- iOS 7.0+ - Deprecated in 15.0
- iPadOS 7.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0

## Declaration

```swift
var userFullName: String! { get }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, readonly) NSString * userFullName;
```

*macOS*

```objc
@property (atomic, readonly) NSString * userFullName;
```

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
- [var username: String!](./username.md)
  The username for this account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/userfullname)*