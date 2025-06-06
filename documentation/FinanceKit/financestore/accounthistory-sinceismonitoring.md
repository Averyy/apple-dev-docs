# accountHistory(since:isMonitoring:)

**Framework**: FinanceKit  
**Kind**: method

Returns a list of accounts a person added since a time specified by the provided financial history token.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func accountHistory(since token: FinanceStore.HistoryToken? = nil, isMonitoring: Bool = true) -> FinanceStore.History<Account>
```

#### Return Value

A `History` that describes the accounts.

#### Discussion

Use this method to list and monitor accounts present in a person’s Wallet. If provided, the framework uses the `since` history token as a starting point to evaluate which accounts to return.

## Parameters

- `isMonitoring`: A Boolean value that indicates if the framework should return a    that indicates the changes to the accounts over time.   Defaults to 

## See Also

- [func accounts(query: AccountQuery) async throws -> [Account]](financestore/accounts(query:).md)
  Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
- [struct AssetAccount](assetaccount.md)
  A structure that describes the characteristics of an asset account.
- [struct LiabilityAccount](liabilityaccount.md)
  A structure that describes the characteristics of a liability account.
- [enum Account](account.md)
  A structure that describes a financial account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/accounthistory(since:ismonitoring:))*