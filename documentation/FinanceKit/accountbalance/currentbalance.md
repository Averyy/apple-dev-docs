# currentBalance

**Framework**: FinanceKit  
**Kind**: property  
**Role**: Instance Property

The balance at a particular moment in time.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let currentBalance: CurrentBalance
```

## Discussion

It can contain an indication of funds immediately available to the customer, fund with all booked transactions (this excludes pending transactions), or both.

## See Also

### Instance Properties
- [let accountID: UUID](./accountid.md)
  The account ID the balance belongs to.
- [var available: Balance?](./available.md)
  The available balance, if present.
- [var booked: Balance?](./booked.md)
  The booked balance, if present.
- [var currencyCode: String](./currencycode.md)
  The balance currency.
- [let id: UUID](./id.md)
  A unique account balance ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountbalance/currentbalance)*