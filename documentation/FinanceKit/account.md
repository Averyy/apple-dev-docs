# Account

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

A structure that describes a financial account.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum Account
```

## Overview

Accounts can include a variety of financial account types such as a bank account, a credit card, or a college fund.

## Topics

### Enumeration Casess
- [case asset(AssetAccount)](./account/asset%28_%29.md)
  An asset account.
- [case liability(LiabilityAccount)](./account/liability%28_%29.md)
  A liability account.
### Instance Properties
- [var accountDescription: String?](./account/accountdescription.md)
  A person’s description of this account.
- [var assetAccount: AssetAccount?](./account/assetaccount.md)
  An asset account.
- [var currencyCode: String](./account/currencycode.md)
  The ISO 4217 currency code that identifies the currency that denominates the account.
- [var displayName: String](./account/displayname.md)
  The name for this account that a person provided.
- [var id: UUID](./account/id.md)
  The unique account ID for this account.
- [var institutionName: String](./account/institutionname.md)
  The name of the institution that holds this account.
- [var liabilityAccount: LiabilityAccount?](./account/liabilityaccount.md)
  A liability account.
- [var openingDate: Date?](./account/openingdate.md)
  The date the account was opened, if known.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accounts
- [func accounts(query: AccountQuery) async throws -> [Account]](./financestore/accounts%28query%29.md)
  Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
- [func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>](./financestore/accounthistory%28since,ismonitoring%29.md)
  Returns a list of accounts a person added since a time specified by the provided financial history token.
- [struct AssetAccount](./assetaccount.md)
  A structure that describes the characteristics of an asset account.
- [struct LiabilityAccount](./liabilityaccount.md)
  A structure that describes the characteristics of a liability account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/account)*