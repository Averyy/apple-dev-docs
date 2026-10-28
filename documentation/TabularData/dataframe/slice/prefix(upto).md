# prefix(upTo:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns a new slice that contains the initial elements of the original slice up to, but not including, the element at a position.

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
func prefix(upTo position: Int) -> DataFrame.Slice
```

## Return Value

A new slice of the underlying data frame.

## Parameters

- `position`: A valid index to an element in the slice.

## See Also

### Creating a Slice by Selecting Rows
- [func prefix(Int) -> DataFrame.Slice](./prefix%28_%29.md)
  Returns a new slice that contains the initial elements of the original slice.
- [func prefix(through: Int) -> DataFrame.Slice](./prefix%28through%29.md)
  Returns a new slice that contains the initial elements of the original slice up to and including the element at a position.
- [func suffix(Int) -> DataFrame.Slice](./suffix%28_%29.md)
  Returns a new slice that contains the final elements of the original slice.
- [func suffix(from: Int) -> DataFrame.Slice](./suffix%28from%29.md)
  Returns a new slice that contains the final elements of the original slice beginning with the element at a position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/prefix(upto:))*