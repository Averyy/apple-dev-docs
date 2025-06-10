# FinanceStore.ContainsOrderResult

**Framework**: FinanceKit  
**Kind**: enum

Result type for queries against the finance store’s orders.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ContainsOrderResult
```

#### Overview

These values represent the possible results of the `containsOrder` method you use to check whether an order you specified exists in the `FinanceStore`.

## Topics

### Operators
- [static func == (FinanceStore.ContainsOrderResult, FinanceStore.ContainsOrderResult) -> Bool](financestore/containsorderresult/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FinanceStore.ContainsOrderResult.exists](financestore/containsorderresult/exists.md)
  The specified order exists.
- [FinanceStore.ContainsOrderResult.newerExists](financestore/containsorderresult/newerexists.md)
  A newer order than the one you specified exists.
- [FinanceStore.ContainsOrderResult.notFound](financestore/containsorderresult/notfound.md)
  The specified order doesn’t exist.
- [FinanceStore.ContainsOrderResult.olderExists](financestore/containsorderresult/olderexists.md)
  A older order than the one you specified exists.
### Instance Properties
- [var hashValue: Int](financestore/containsorderresult/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](financestore/containsorderresult/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [FinanceStore.ContainsOrderResult.AllCases](financestore/containsorderresult/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [FinanceStore.ContainsOrderResult]](financestore/containsorderresult/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](financestore/containsorderresult/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FinanceStore.DataType](financestore/datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.SaveOrderResult](financestore/saveorderresult.md)
  Result type for the finance store’s save order method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/containsorderresult)*