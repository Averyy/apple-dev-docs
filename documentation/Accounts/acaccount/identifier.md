# identifier

**Framework**: Accounts  
**Kind**: property

A unique identifier for this account.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
weak var identifier: NSString! { get }
```

#### Discussion

Use the [`account(withIdentifier:)`](acaccountstore/account(withidentifier:).md) method to get an account with the specified identifier.

## See Also

- [var accountDescription: String!](acaccount/accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](acaccount/accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](acaccount/credential.md)
  The credential used to authenticate the user of this account.
- [var username: String!](acaccount/username.md)
  The username for this account.
- [var userFullName: String!](acaccount/userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/identifier)*