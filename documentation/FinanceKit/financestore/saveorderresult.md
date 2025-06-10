# FinanceStore.SaveOrderResult

**Framework**: FinanceKit  
**Kind**: enum

Result type for the finance store’s save order method.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum SaveOrderResult
```

## Topics

### Operators
- [static func == (FinanceStore.SaveOrderResult, FinanceStore.SaveOrderResult) -> Bool](financestore/saveorderresult/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FinanceStore.SaveOrderResult.added](financestore/saveorderresult/added.md)
  The framework added the order to the finance store.
- [FinanceStore.SaveOrderResult.cancelled](financestore/saveorderresult/cancelled.md)
  The individual canceled the order.
- [FinanceStore.SaveOrderResult.newerExisting](financestore/saveorderresult/newerexisting.md)
  There’s a newer, existing order already in the finance store.
### Instance Properties
- [var hashValue: Int](financestore/saveorderresult/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](financestore/saveorderresult/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [FinanceStore.SaveOrderResult.AllCases](financestore/saveorderresult/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [FinanceStore.SaveOrderResult]](financestore/saveorderresult/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](financestore/saveorderresult/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.ContainsOrderResult](financestore/containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.DataType](financestore/datatype.md)
  Values that describe the kinds of data in the finance store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/saveorderresult)*