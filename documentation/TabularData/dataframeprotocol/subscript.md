# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Required**: Yes

Accesses a slice of the data frame type with an index range.

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
subscript(range: Range<Int>) -> DataFrame.Slice { get set }
```

## Parameters

- `range`: An integer range.

## See Also

- [subscript<R>(R) -> DataFrame.Slice](dataframeprotocol/subscript(_:)-8hly3.md)
  Accesses rows of a data frame type with an index range expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/subscript(_:))*