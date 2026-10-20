# accountTypeDescription

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

A human-readable description of the account type.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
var accountTypeDescription: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * accountTypeDescription;
```

## See Also

### Accessing Properties
- [var accessGranted: Bool](./accessgranted.md)
  A Boolean value indicating whether the user granted the application access to accounts of this type.
- [var identifier: String!](./identifier.md)
  The unique identifier for the account type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccounttype/accounttypedescription)*