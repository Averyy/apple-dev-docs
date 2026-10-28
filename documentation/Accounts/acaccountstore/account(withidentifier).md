# account(withIdentifier:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Returns the account with the specified identifier.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func account(withIdentifier identifier: String!) -> ACAccount!
```

```objc
- (ACAccount *) accountWithIdentifier:(NSString *) identifier;
```

## Return Value

The account that matches the value specified in `identifier`.

## Parameters

- `identifier`: A unique identifier for an account.

## See Also

### Getting Accounts
- [var accounts: NSArray!](./accounts.md)
  The accounts managed by this account store.
- [func accounts(with: ACAccountType!) -> [Any]!](./accounts%28with%29.md)
  Returns all accounts of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/account(withidentifier:))*