# ACAccountType

**Framework**: Accounts  
**Kind**: class

An object that encapsulates information about all accounts of a particular type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
class ACAccountType
```

#### Overview

You don’t create account type objects directly. To obtain an account type object, use the [`accountType(withAccountTypeIdentifier:)`](acaccountstore/accounttype(withaccounttypeidentifier:).md) method or the [`accountType`](acaccount/accounttype.md) property of an account object. Use the [`accounts(with:)`](acaccountstore/accounts(with:).md) method to obtain all accounts of a particular type.

## Topics

### Accessing Properties
- [var accessGranted: Bool](acaccounttype/accessgranted.md)
  A Boolean value indicating whether the user granted the application access to accounts of this type.
- [var accountTypeDescription: String!](acaccounttype/accounttypedescription.md)
  A human-readable description of the account type.
- [var identifier: String!](acaccounttype/identifier.md)
  The unique identifier for the account type.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccounttype)*