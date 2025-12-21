# FinanceStore.History

**Framework**: FinanceKit  
**Kind**: struct

A structure the framework uses to collect and iterate over finance store model objects.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct History<Model> where Model : Identifiable
```

## Topics

### Structures
- [FinanceStore.History.Iterator](financestore/history/iterator.md)
  The type that allows iteration over an array’s elements.
### Instance Methods
- [func makeAsyncIterator() -> FinanceStore.History<Model>.Iterator](financestore/history/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [FinanceStore.History.AsyncIterator](financestore/history/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [FinanceStore.History.Element](financestore/history/element.md)
  An alias for the type that this asynchronous sequence holds.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.Changes](financestore/changes.md)
  A structure that records changes to the finance store.
- [FinanceStore.HistoryToken](financestore/historytoken.md)
  A structure that describes the starting point to use for financial data queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/history)*