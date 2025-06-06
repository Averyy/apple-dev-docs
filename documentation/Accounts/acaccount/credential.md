# credential

**Framework**: Accounts  
**Kind**: property

The credential used to authenticate the user of this account.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var credential: ACAccountCredential! { get set }
```

#### Discussion

This property is required and must be set before the account is saved. For privacy reasons, this property is inaccessible after the account is saved.

## See Also

- [var accountDescription: String!](acaccount/accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](acaccount/accounttype.md)
  The type of service account.
- [var identifier: NSString!](acaccount/identifier.md)
  A unique identifier for this account.
- [var username: String!](acaccount/username.md)
  The username for this account.
- [var userFullName: String!](acaccount/userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/credential)*