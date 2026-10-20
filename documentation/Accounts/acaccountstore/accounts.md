# accounts

**Framework**: Accounts  
**Kind**: property  
**Role**: Instance Property

The accounts managed by this account store.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
weak var accounts: NSArray! { get }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, weak, readonly) NSArray * accounts;
```

*macOS*

```objc
@property (atomic, weak, readonly) NSArray * accounts;
```

## See Also

### Getting Accounts
- [func account(withIdentifier: String!) -> ACAccount!](./account%28withidentifier%29.md)
  Returns the account with the specified identifier.
- [func accounts(with: ACAccountType!) -> [Any]!](./accounts%28with%29.md)
  Returns all accounts of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/accounts)*