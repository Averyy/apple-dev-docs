# accountType

**Framework**: Accounts  
**Kind**: property

The type of service account.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var accountType: ACAccountType! { get set }
```

#### Discussion

This property is required. You specify the account type using the [`init(accountType:)`](acaccount/init(accounttype:).md) method. You can use the [`accounts(with:)`](acaccountstore/accounts(with:).md) method to retrieve all accounts of a particular type.

## See Also

- [var accountDescription: String!](acaccount/accountdescription.md)
  A human-readable description of the account.
- [var credential: ACAccountCredential!](acaccount/credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](acaccount/identifier.md)
  A unique identifier for this account.
- [var username: String!](acaccount/username.md)
  The username for this account.
- [var userFullName: String!](acaccount/userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/accounttype)*