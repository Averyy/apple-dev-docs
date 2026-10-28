# accessGranted

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user granted the application access to accounts of this type.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
var accessGranted: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL accessGranted;
```

## Discussion

[`true`](../../Swift/true.md) if the application has access to accounts of this type; otherwise [`false`](../../Swift/false.md).

## See Also

### Accessing Properties
- [var accountTypeDescription: String!](./accounttypedescription.md)
  A human-readable description of the account type.
- [var identifier: String!](./identifier.md)
  The unique identifier for the account type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccounttype/accessgranted)*