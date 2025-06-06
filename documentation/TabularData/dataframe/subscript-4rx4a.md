# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses rows of a data frame type with an index range expression.

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
subscript<R>(r: R) -> DataFrame.Slice where R : RangeExpression, R.Bound == Int { get set }
```

## Parameters

- `r`: An integer range expression.

## See Also

- [subscript(Range<Int>) -> DataFrame.Slice](dataframe/subscript(_:)-8wcl1.md)
  Accesses a slice of the data frame type with an index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/subscript(_:)-4rx4a)*