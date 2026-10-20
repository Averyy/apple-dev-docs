# ACAccountType

**Framework**: Accounts  
**Kind**: class  
**Role**: Class

An object that encapsulates information about all accounts of a particular type.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
class ACAccountType
```

```objc
@interface ACAccountType : NSObject
```

#### Overview

You don’t create account type objects directly. To obtain an account type object, use the [`accountType(withAccountTypeIdentifier:)`](./acaccountstore/accounttype%28withaccounttypeidentifier%29.md) method or the [`accountType`](./acaccount/accounttype.md) property of an account object. Use the [`accounts(with:)`](./acaccountstore/accounts%28with%29.md) method to obtain all accounts of a particular type.

## Topics

### Accessing Properties
- [var accessGranted: Bool](./acaccounttype/accessgranted.md)
  A Boolean value indicating whether the user granted the application access to accounts of this type.
- [var accountTypeDescription: String!](./acaccounttype/accounttypedescription.md)
  A human-readable description of the account type.
- [var identifier: String!](./acaccounttype/identifier.md)
  The unique identifier for the account type.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccounttype)*