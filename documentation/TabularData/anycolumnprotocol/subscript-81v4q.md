# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Required**: Yes

Retrieves a contiguous subrange of the column type’s elements.

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
subscript(range: Range<Int>) -> AnyColumnSlice { get }
```

## Parameters

- `range`: An integer range of valid indices in the column.

## See Also

- [subscript(Int) -> Any?](anycolumnprotocol/subscript(_:)-1dl8y.md)
  Retrieves an element at a position in the column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnprotocol/subscript(_:)-81v4q)*