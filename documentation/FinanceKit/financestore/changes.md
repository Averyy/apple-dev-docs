# FinanceStore.Changes

**Framework**: FinanceKit  
**Kind**: struct  
**Role**: Structure

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
- [let deleted: [Model.ID]](./changes/deleted.md)
  An array of model objects identifiers that the framework deleted from the finance store.
- [let inserted: [Model]](./changes/inserted.md)
  An array of model objects the framework inserted into the finance store.
- [let newToken: FinanceStore.HistoryToken](./changes/newtoken.md)
  An updated history token that you can use to query more historical data.
- [let updated: [Model]](./changes/updated.md)
  An array of model objects that the framework updated in the finance store.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Structures
- [FinanceStore.History](./history.md)
  A structure the framework uses to collect and iterate over finance store model objects.
- [FinanceStore.HistoryToken](./historytoken.md)
  A structure that describes the starting point to use for financial data queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/changes)*