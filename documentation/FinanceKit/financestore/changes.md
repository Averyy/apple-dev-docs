# FinanceStore.Changes

**Framework**: FinanceKit  
**Kind**: struct

A structure that records changes to the finance store.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Changes<Model> where Model : Identifiable
```

## Topics

### Instance Properties
- [let deleted: [Model.ID]](financestore/changes/deleted.md)
  An array of model objects identifiers that the framework deleted from the finance store.
- [let inserted: [Model]](financestore/changes/inserted.md)
  An array of model objects the framework inserted into the finance store.
- [let newToken: FinanceStore.HistoryToken](financestore/changes/newtoken.md)
  An updated history token that you can use to query more historical data.
- [let updated: [Model]](financestore/changes/updated.md)
  An array of model objects that the framework updated in the finance store.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.History](financestore/history.md)
  A structure the framework uses to collect and iterate over finance store model objects.
- [FinanceStore.HistoryToken](financestore/historytoken.md)
  A structure that describes the starting point to use for financial data queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/changes)*