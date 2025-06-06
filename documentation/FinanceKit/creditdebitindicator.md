# CreditDebitIndicator

**Framework**: FinanceKit  
**Kind**: enum

Values that the framework uses to describe transactions as credits or debits.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum CreditDebitIndicator
```

## Topics

### Enumeration Cases
- [CreditDebitIndicator.credit](creditdebitindicator/credit.md)
  A value that indicates an amount which increases an asset or decreases a liability.
- [CreditDebitIndicator.debit](creditdebitindicator/debit.md)
  A value that indicates an amount which increases a liability or decreases an asset.
### Initializers
- [init?(rawValue: Int16)](creditdebitindicator/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int16](creditdebitindicator/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [CreditDebitIndicator.AllCases](creditdebitindicator/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [CreditDebitIndicator.RawValue](creditdebitindicator/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [CreditDebitIndicator]](creditdebitindicator/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](creditdebitindicator/equatable-implementations.md)
- [RawRepresentable Implementations](creditdebitindicator/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](financestore/accountbalancehistory(foraccountid:since:ismonitoring:).md)
  Returns the account balance history since a time specified by the provided financial history token.
- [struct AccountBalance](accountbalance.md)
  A structure that describes the financial balance of an account at a specific point in time.
- [struct AccountBalanceQuery](accountbalancequery.md)
  A structure that defines an account balance query.
- [struct Balance](balance.md)
  A structure that describes an account balance.
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/creditdebitindicator)*