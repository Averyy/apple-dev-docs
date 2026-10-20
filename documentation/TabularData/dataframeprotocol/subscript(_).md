# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript  
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

## Default Implementations

### DataFrameProtocol Implementations
- [subscript(Range<Int>) -> DataFrame.Slice](./subscript%28_%29-2p37h.md)
  Accesses a slice of the data frame type with an index range.
- [subscript<R>(R) -> DataFrame.Slice](./subscript%28_%29-8hly3.md)
  Accesses rows of a data frame type with an index range expression.

## See Also

### Accessing Rows
- [subscript<R>(R) -> DataFrame.Slice](./subscript%28_%29-8hly3.md)
  Accesses rows of a data frame type with an index range expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/subscript(_:))*