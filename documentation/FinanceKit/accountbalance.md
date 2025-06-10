# AccountBalance

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes the financial balance of an account at a specific point in time. The financial balance of an account at a specific point in time.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AccountBalance
```

## Topics

### Operators
- [static func == (AccountBalance, AccountBalance) -> Bool](accountbalance/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](accountbalance/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let accountID: UUID](accountbalance/accountid.md)
  The account ID the balance belongs to.
- [var available: Balance?](accountbalance/available.md)
  The available balance, if present.
- [var booked: Balance?](accountbalance/booked.md)
  The booked balance, if present.
- [var currencyCode: String](accountbalance/currencycode.md)
  The balance currency.
- [let currentBalance: CurrentBalance](accountbalance/currentbalance.md)
  The balance at a particular moment in time.
- [let id: UUID](accountbalance/id-swift.property.md)
  A unique account balance ID.
### Instance Methods
- [func encode(to: any Encoder) throws](accountbalance/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [AccountBalance.ID](accountbalance/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](accountbalance/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](financestore/accountbalancehistory(foraccountid:since:ismonitoring:).md)
  Returns the account balance history since a time specified by the provided financial history token.
- [struct AccountBalanceQuery](accountbalancequery.md)
  A structure that defines an account balance query.
- [struct Balance](balance.md)
  A structure that describes an account balance.
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountbalance)*