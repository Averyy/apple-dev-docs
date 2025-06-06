# account(withIdentifier:)

**Framework**: Accounts  
**Kind**: method

Returns the account with the specified identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func account(withIdentifier identifier: String!) -> ACAccount!
```

#### Return Value

The account that matches the value specified in `identifier`.

## Parameters

- `identifier`: A unique identifier for an account.

## See Also

- [var accounts: NSArray!](acaccountstore/accounts.md)
  The accounts managed by this account store.
- [func accounts(with: ACAccountType!) -> [Any]!](acaccountstore/accounts(with:).md)
  Returns all accounts of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/account(withidentifier:))*