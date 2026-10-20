# accounts(with:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Returns all accounts of the specified type.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func accounts(with accountType: ACAccountType!) -> [Any]!
```

```objc
- (NSArray *) accountsWithAccountType:(ACAccountType *) accountType;
```

#### Return Value

All accounts that match `accountType`.

## Parameters

- `accountType`: The type of an account.

## See Also

### Getting Accounts
- [var accounts: NSArray!](./accounts.md)
  The accounts managed by this account store.
- [func account(withIdentifier: String!) -> ACAccount!](./account%28withidentifier%29.md)
  Returns the account with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/accounts(with:))*