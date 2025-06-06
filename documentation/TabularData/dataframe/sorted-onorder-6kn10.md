# sorted(on:order:)

**Framework**: TabularData  
**Kind**: method

Generates a data frame by copying the data frame’s rows and then sorting the rows according to a column that you select by its column identifier.

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
func sorted<T>(on columnID: ColumnID<T>, order: Order = .ascending) -> DataFrame where T : Comparable
```

#### Discussion

> **Note**: Elements with a value of `nil` are less than all non-`nil` values.

Elements with a value of `nil` are less than all non-`nil` values.

## Parameters

- `order`: A sorting order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/sorted(on:order:)-6kn10)*