# FinanceStore.DataType

**Framework**: FinanceKit  
**Kind**: enum

Values that describe the kinds of data in the finance store.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum DataType
```

## Topics

### Operators
- [static func == (FinanceStore.DataType, FinanceStore.DataType) -> Bool](financestore/datatype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FinanceStore.DataType.financialData](financestore/datatype/financialdata.md)
  The value that describes financial data, such as account information.
- [FinanceStore.DataType.orders](financestore/datatype/orders.md)
  The value that describes orders records, such as purchases.
### Instance Properties
- [var hashValue: Int](financestore/datatype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](financestore/datatype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](financestore/datatype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [FinanceStore.ContainsOrderResult](financestore/containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.SaveOrderResult](financestore/saveorderresult.md)
  Result type for the finance store’s save order method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/datatype)*