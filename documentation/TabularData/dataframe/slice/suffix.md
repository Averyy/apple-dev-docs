# suffix(_:)

**Framework**: TabularData  
**Kind**: method

Returns a new slice that contains the final elements of the original slice.

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
func suffix(_ length: Int) -> DataFrame.Slice
```

#### Return Value

A new slice of the underlying data frame.

## Parameters

- `length`: The number of elements in the new slice.   The length must be greater than or equal to zero and less than or equal to the number of elements   in the original slice.

## See Also

- [func prefix(Int) -> DataFrame.Slice](dataframe/slice/prefix(_:).md)
  Returns a new slice that contains the initial elements of the original slice.
- [func prefix(upTo: Int) -> DataFrame.Slice](dataframe/slice/prefix(upto:).md)
  Returns a new slice that contains the initial elements of the original slice up to, but not including, the element at a position.
- [func prefix(through: Int) -> DataFrame.Slice](dataframe/slice/prefix(through:).md)
  Returns a new slice that contains the initial elements of the original slice up to and including the element at a position.
- [func suffix(from: Int) -> DataFrame.Slice](dataframe/slice/suffix(from:).md)
  Returns a new slice that contains the final elements of the original slice beginning with the element at a position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/suffix(_:))*