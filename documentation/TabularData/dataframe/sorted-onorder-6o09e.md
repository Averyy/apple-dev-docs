# sorted(on:order:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its name.

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
func sorted(on columnName: String, order: Order = .ascending) -> DataFrame
```

#### Discussion

This is a convenience method that only works for columns of the following types:

- [`Bool`](https://developer.apple.com/documentation/Swift/Bool)
- [`Int`](https://developer.apple.com/documentation/Swift/Int)
- [`Float`](https://developer.apple.com/documentation/Swift/Float)
- [`Double`](https://developer.apple.com/documentation/Swift/Double)
- [`Date`](https://developer.apple.com/documentation/Foundation/Date)

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `columnName`: The name of a column.
- `order`: A sorting order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/sorted(on:order:)-6o09e)*