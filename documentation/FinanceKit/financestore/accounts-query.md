# accounts(query:)

**Framework**: FinanceKit  
**Kind**: method

Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func accounts(query: AccountQuery) async throws -> [Account]
```

#### Return Value

An array of [`Account`](account.md) structures.

## Parameters

- `query`: An   that describes the kinds of accounts to look for.

## See Also

- [func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>](financestore/accounthistory(since:ismonitoring:).md)
  Returns a list of accounts a person added since a time specified by the provided financial history token.
- [struct AssetAccount](assetaccount.md)
  A structure that describes the characteristics of an asset account.
- [struct LiabilityAccount](liabilityaccount.md)
  A structure that describes the characteristics of a liability account.
- [enum Account](account.md)
  A structure that describes a financial account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/accounts(query:))*