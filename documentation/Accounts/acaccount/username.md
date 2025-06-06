# username

**Framework**: Accounts  
**Kind**: property

The username for this account.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var username: String! { get set }
```

#### Discussion

This property must be set before the account is saved. After the account is saved, this property is available if the user grants the application access to this account; otherwise it’s `nil`.

## See Also

- [var accountDescription: String!](acaccount/accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](acaccount/accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](acaccount/credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](acaccount/identifier.md)
  A unique identifier for this account.
- [var userFullName: String!](acaccount/userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/username)*