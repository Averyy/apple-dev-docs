# ACAccount

**Framework**: Accounts  
**Kind**: class

The information associated with one of the user’s accounts.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
class ACAccount
```

#### Overview

An [`ACAccount`](acaccount.md) object encapsulates information about a user account stored in the Accounts database. You can create and retrieve accounts using an [`ACAccountStore`](acaccountstore.md) object. The [`ACAccountStore`](acaccountstore.md) object provides an interface to the persistent Accounts database. For each user, all account objects belong to a single [`ACAccountStore`](acaccountstore.md) object.

## Topics

### Creating an Account Object
- [init!(accountType: ACAccountType!)](acaccount/init(accounttype:).md)
  Initializes a new account of the specified type.
### Accessing Properties
- [var accountDescription: String!](acaccount/accountdescription.md)
  A human-readable description of the account.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ACAccountStore](acaccountstore.md)
  The object you use to request, manage, and store the user’s account information.
- [class ACAccountCredential](acaccountcredential.md)
  A credential object that encapsulates the information needed to authenticate a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount)*