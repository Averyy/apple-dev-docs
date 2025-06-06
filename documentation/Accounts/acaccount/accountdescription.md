# accountDescription

**Framework**: Accounts  
**Kind**: property

A human-readable description of the account.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var accountDescription: String! { get set }
```

#### Discussion

This property is available if the user grants the application access to this account; otherwise it’s `nil`.

## See Also

- [var accountType: ACAccountType!](acaccount/accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](acaccount/credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](acaccount/identifier.md)
  A unique identifier for this account.
- [var username: String!](acaccount/username.md)
  The username for this account.
- [var userFullName: String!](acaccount/userfullname.md)
  The full name associated with the user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/accountdescription)*