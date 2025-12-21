# currencyCode

**Framework**: FinanceKit  
**Kind**: property

The balance currency.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var currencyCode: String { get }
```

#### Discussion

This is the same across available and booked balances.

## See Also

- [let accountID: UUID](accountbalance/accountid.md)
  The account ID the balance belongs to.
- [var available: Balance?](accountbalance/available.md)
  The available balance, if present.
- [var booked: Balance?](accountbalance/booked.md)
  The booked balance, if present.
- [let currentBalance: CurrentBalance](accountbalance/currentbalance.md)
  The balance at a particular moment in time.
- [let id: UUID](accountbalance/id.md)
  A unique account balance ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountbalance/currencycode)*