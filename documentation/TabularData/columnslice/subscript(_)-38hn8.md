# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses an element at an index.

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
subscript(position: Int) -> ColumnSlice<WrappedElement>.Element { get set }
```

## Parameters

- `position`: A valid index to an element in the column slice.

## See Also

### Accessing Elements
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](./subscript%28_%29-7lrhk.md)
  Accesses a contiguous range of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/subscript(_:)-38hn8)*