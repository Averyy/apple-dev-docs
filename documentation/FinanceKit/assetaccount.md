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

### Operators
- [static func == (AssetAccount, AssetAccount) -> Bool](assetaccount/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](assetaccount/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let accountDescription: String?](assetaccount/accountdescription.md)
  The description of the account.
- [let currencyCode: String](assetaccount/currencycode.md)
  ISO 4217 currency code that identifies the currency in which the account is held.
- [let displayName: String](assetaccount/displayname.md)
  The name for the account given by a person.
- [let id: UUID](assetaccount/id-swift.property.md)
  A unique account identifier.
- [let institutionName: String](assetaccount/institutionname.md)
  The name of the institution that holds the account.
- [let openingDate: Date?](assetaccount/openingdate.md)
  The date the account was opened, if known.
### Instance Methods
- [func encode(to: any Encoder) throws](assetaccount/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [AssetAccount.ID](assetaccount/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](assetaccount/equatable-implementations.md)

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