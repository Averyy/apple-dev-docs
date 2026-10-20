# accounts(with:)

**Framework**: Accounts  
**Kind**: method

Returns all accounts of the specified type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func accounts(with accountType: ACAccountType!) -> [Any]!
```

#### Return Value

All accounts that match `accountType`.

## Parameters

- `accountType`: The type of an account.

## See Also

- [var accounts: NSArray!](acaccountstore/accounts.md)
  The accounts managed by this account store.
- [func account(withIdentifier: String!) -> ACAccount!](acaccountstore/account(withidentifier:).md)
  Returns the account with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/accounts(with:))*