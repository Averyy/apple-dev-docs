# predicate(bookedSince:until:)

**Framework**: FinanceKit  
**Kind**: method

A predicate that returns booked account balances since a specified date until another date.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
static func predicate(bookedSince startDate: Date, until endDate: Date? = nil) -> Predicate<AccountBalance>
```

## Parameters

- `startDate`: The date to start collecting account balances.
- `endDate`: The date to end collection account balances. This parameter is optional. If   this parameter isn’t included,   the method returns all account balances since the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountbalancequery/predicate(bookedsince:until:))*