# Balance

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes an account balance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Balance
```

## Topics

### Operators
- [static func == (Balance, Balance) -> Bool](balance/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](balance/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let amount: CurrencyAmount](balance/amount.md)
  The amount of the balance.
- [let asOfDate: Date](balance/asofdate.md)
  The date and time the system calculated the balance.
- [let creditDebitIndicator: CreditDebitIndicator](balance/creditdebitindicator.md)
  A value that indicates whether the balance is a credit or a debit balance.
- [var hashValue: Int](balance/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](balance/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](balance/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](balance/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/balance)*