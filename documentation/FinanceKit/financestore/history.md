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
  The type that allows iteration over an array’s elements
### Instance Methods
- [func makeAsyncIterator() -> FinanceStore.History<Model>.Iterator](financestore/history/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [FinanceStore.History.AsyncIterator](financestore/history/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence
- [FinanceStore.History.Element](financestore/history/element.md)
  An alias for the type that this asynchronous sequence holds.
### Default Implementations
- [AsyncSequence Implementations](financestore/history/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/history)*