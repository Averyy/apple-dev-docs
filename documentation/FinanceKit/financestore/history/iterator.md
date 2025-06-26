# FinanceStore.History.Iterator

**Framework**: FinanceKit  
**Kind**: struct

The type that allows iteration over an array’s elements.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async throws -> FinanceStore.Changes<Model>?](financestore/history/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [FinanceStore.History.Iterator.Element](financestore/history/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](financestore/history/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/history/iterator)*