# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a contiguous range of elements.

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
subscript(range: Range<Int>) -> ColumnSlice<WrappedElement> { get set }
```

## Parameters

- `range`: A range of valid indices in the column slice.

## See Also

### Accessing Elements
- [subscript(Int) -> ColumnSlice<WrappedElement>.Element](./subscript%28_%29-38hn8.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/subscript(_:)-7lrhk)*