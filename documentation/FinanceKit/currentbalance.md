# CurrentBalance

**Framework**: FinanceKit  
**Kind**: enum

Values that describe the state of an account’s credit balance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum CurrentBalance
```

## Topics

### Operators
- [static func == (CurrentBalance, CurrentBalance) -> Bool](currentbalance/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [CurrentBalance.available(_:)](currentbalance/available(_:).md)
  Only the available balance is present.
- [case availableAndBooked(available: Balance, booked: Balance)](currentbalance/availableandbooked(available:booked:).md)
  Both available and booked balances are present.
- [CurrentBalance.booked(_:)](currentbalance/booked(_:).md)
  Only the booked balance is present.
### Initializers
- [init(from: any Decoder) throws](currentbalance/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](currentbalance/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](currentbalance/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](currentbalance/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](currentbalance/equatable-implementations.md)

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
- [struct Balance](balance.md)
  A structure that describes an account balance.
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/currentbalance)*