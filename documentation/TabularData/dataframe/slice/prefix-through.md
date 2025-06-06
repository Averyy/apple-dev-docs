# prefix(through:)

**Framework**: TabularData  
**Kind**: method

Returns a new slice that contains the initial elements of the original slice up to and including the element at a position.

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
func prefix(through position: Int) -> DataFrame.Slice
```

#### Return Value

A new slice of the underlying data frame.

## Parameters

- `position`: A valid index to an element in the slice.

## See Also

- [func prefix(Int) -> DataFrame.Slice](dataframe/slice/prefix(_:).md)
  Returns a new slice that contains the initial elements of the original slice.
- [func prefix(upTo: Int) -> DataFrame.Slice](dataframe/slice/prefix(upto:).md)
  Returns a new slice that contains the initial elements of the original slice up to, but not including, the element at a position.
- [func suffix(Int) -> DataFrame.Slice](dataframe/slice/suffix(_:).md)
  Returns a new slice that contains the final elements of the original slice.
- [func suffix(from: Int) -> DataFrame.Slice](dataframe/slice/suffix(from:).md)
  Returns a new slice that contains the final elements of the original slice beginning with the element at a position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/prefix(through:))*