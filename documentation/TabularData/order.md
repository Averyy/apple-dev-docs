# Order

**Framework**: TabularData  
**Kind**: enum

A type that represents a sort ordering.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Order
```

## Topics

### Getting the Properties
- [Order.ascending](order/ascending.md)
  A sort ordering that starts with the lowest value and monotonically proceeds to higher values.
- [Order.descending](order/descending.md)
  A sort ordering that starts with the highest value and monotonically proceeds to lower values.
- [func areOrdered<T>(T, T) -> Bool](order/areordered(_:_:).md)
  Returns a Boolean that indicates whether the comparable types match the order’s state.
### Operators
- [static func == (Order, Order) -> Bool](order/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](order/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](order/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](order/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ColumnID](columnid.md)
  A column identifier that stores a column’s name and the type of its elements.
- [struct FormattingOptions](formattingoptions.md)
  A set of parameters that indicate how to present the contents of data frame or column types to a printable string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/order)*