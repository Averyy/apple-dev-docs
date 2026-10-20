# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a row at an index.

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
subscript(position: Int) -> DataFrame.Row { get set }
```

## Parameters

- `position`: A valid index to a row in the collection.

## See Also

### Accessing Elements
- [subscript(Range<Int>) -> DataFrame.Rows](./subscript%28_%29-2qzx7.md)
  Returns a row collection from an index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/subscript(_:)-3f938)*