# Account

**Framework**: FinanceKit  
**Kind**: enum

A structure that describes a financial account.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum Account
```

#### Overview

Accounts can include a variety of financial account types such as a bank account, a credit card, or a college fund.

## Topics

### Operators
- [static func == (Account, Account) -> Bool](account/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [case asset(AssetAccount)](account/asset(_:).md)
  An asset account.
- [case liability(LiabilityAccount)](account/liability(_:).md)
  A liability account.
### Initializers
- [init(from: any Decoder) throws](account/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var accountDescription: String?](account/accountdescription.md)
  A person’s description of this account.
- [var assetAccount: AssetAccount?](account/assetaccount.md)
  An asset account.
- [var currencyCode: String](account/currencycode.md)
  The ISO 4217 currency code that identifies the currency that denominates the account.
- [var displayName: String](account/displayname.md)
  The name for this account that a person provided.
- [var id: UUID](account/id-swift.property.md)
  The unique account ID for this account.
- [var institutionName: String](account/institutionname.md)
  The name of the institution that holds this account.
- [var liabilityAccount: LiabilityAccount?](account/liabilityaccount.md)
  A liability account.
- [var openingDate: Date?](account/openingdate.md)
  The date the account was opened, if known.
### Instance Methods
- [func encode(to: any Encoder) throws](account/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [typealias ID](account/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](account/equatable-implementations.md)

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
- [struct AssetAccount](assetaccount.md)
  A structure that describes the characteristics of an asset account.
- [struct LiabilityAccount](liabilityaccount.md)
  A structure that describes the characteristics of a liability account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/account)*