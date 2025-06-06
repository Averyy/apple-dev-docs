# areOrdered(_:_:)

**Framework**: TabularData  
**Kind**: method

Returns a Boolean that indicates whether the comparable types match the order’s state.

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
func areOrdered<T>(_ lhs: T, _ rhs: T) -> Bool where T : Comparable
```

## Parameters

- `lhs`: A comparable type.
- `rhs`: Another comparable type.

## See Also

- [Order.ascending](order/ascending.md)
  A sort ordering that starts with the lowest value and monotonically proceeds to higher values.
- [Order.descending](order/descending.md)
  A sort ordering that starts with the highest value and monotonically proceeds to lower values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/order/areordered(_:_:))*