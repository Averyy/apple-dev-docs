# AssetAccount

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes the characteristics of an asset account.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AssetAccount
```

#### Overview

An asset account includes accounts such as a bank account or a savings account.

## Topics

### Instance Properties
- [let accountDescription: String?](assetaccount/accountdescription.md)
  The description of the account.
- [let currencyCode: String](assetaccount/currencycode.md)
  ISO 4217 currency code that identifies the currency in which the account is held.
- [let displayName: String](assetaccount/displayname.md)
  The name for the account given by a person.
- [let id: UUID](assetaccount/id.md)
  A unique account identifier.
- [let institutionName: String](assetaccount/institutionname.md)
  The name of the institution that holds the account.
- [let openingDate: Date?](assetaccount/openingdate.md)
  The date the account was opened, if known.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accounts(query: AccountQuery) async throws -> [Account]](financestore/accounts(query:).md)
  Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
- [func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>](financestore/accounthistory(since:ismonitoring:).md)
  Returns a list of accounts a person added since a time specified by the provided financial history token.
- [struct LiabilityAccount](liabilityaccount.md)
  A structure that describes the characteristics of a liability account.
- [enum Account](account.md)
  A structure that describes a financial account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/assetaccount)*