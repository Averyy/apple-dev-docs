# suffix(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns a slice that contains the final rows up to a maximum length.

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
func suffix(_ maxLength: Int) -> DataFrame.Slice
```

## Parameters

- `maxLength`: The maximum number of rows.

## See Also

### Creating a slice by selecting rows
- [func prefix(Int) -> DataFrame.Slice](./prefix%28_%29.md)
  Returns a slice that contains the initial rows up to a maximum length.
- [subscript<C>(C) -> DataFrame.Slice](./subscript%28_%29-6tuca.md)
  Returns a slice of the rows by masking its elements with a Boolean column.
- [subscript(Range<Int>) -> DataFrame.Slice](../dataframeprotocol/subscript%28_%29.md)
  Accesses a slice of the data frame type with an index range.
- [subscript<R>(R) -> DataFrame.Slice](../dataframeprotocol/subscript%28_%29-8hly3.md)
  Accesses rows of a data frame type with an index range expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/suffix(_:))*