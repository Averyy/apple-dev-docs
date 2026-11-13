# ==(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Returns a Boolean that indicates whether the column slices are equal.

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
static func == (lhs: DiscontiguousColumnSlice<WrappedElement>, rhs: DiscontiguousColumnSlice<WrappedElement>) -> Bool
```

Available when `WrappedElement` conforms to `Equatable`.

## Parameters

- `lhs`: A discontiguous column slice.
- `rhs`: Another discontiguous column slice.

## See Also

### Comparing two column slices
- [static func != (Self, Self.Element) -> [Bool]](../columnprotocol/noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](../columnprotocol/noteq%28_,_%29-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/==(_:_:))*