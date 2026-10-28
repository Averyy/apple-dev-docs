# ACAccount

**Framework**: Accounts  
**Kind**: class  
**Role**: Class

The information associated with one of the user’s accounts.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
class ACAccount
```

```objc
@interface ACAccount : NSObject
```

## Overview

An [`ACAccount`](./acaccount.md) object encapsulates information about a user account stored in the Accounts database. You can create and retrieve accounts using an [`ACAccountStore`](./acaccountstore.md) object. The [`ACAccountStore`](./acaccountstore.md) object provides an interface to the persistent Accounts database. For each user, all account objects belong to a single [`ACAccountStore`](./acaccountstore.md) object.

## Topics

### Creating an Account Object
- [init!(accountType: ACAccountType!)](./acaccount/init%28accounttype%29.md)
  Initializes a new account of the specified type.
### Accessing Properties
- [var accountDescription: String!](./acaccount/accountdescription.md)
  A human-readable description of the account.
- [var accountType: ACAccountType!](./acaccount/accounttype.md)
  The type of service account.
- [var credential: ACAccountCredential!](./acaccount/credential.md)
  The credential used to authenticate the user of this account.
- [var identifier: NSString!](./acaccount/identifier.md)
  A unique identifier for this account.
- [var username: String!](./acaccount/username.md)
  The username for this account.
- [var userFullName: String!](./acaccount/userfullname.md)
  The full name associated with the user account.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Account Management
- [class ACAccountStore](./acaccountstore.md)
  The object you use to request, manage, and store the user’s account information.
- [class ACAccountCredential](./acaccountcredential.md)
  A credential object that encapsulates the information needed to authenticate a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount)*