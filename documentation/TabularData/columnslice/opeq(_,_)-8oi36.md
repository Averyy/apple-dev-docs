# /=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Modifies an integer column slice by dividing each element by a value.

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
static func /= (lhs: inout ColumnSlice<WrappedElement>, rhs: WrappedElement) where WrappedElement : BinaryInteger
```

## Parameters

- `lhs`: A column slice.
- `rhs`: A value of the same type as the column’s elements.

## See Also

### Modifying a Column Slice with a Value
- [static func += (inout ColumnSlice<WrappedElement>, WrappedElement)](./pluseq%28_,_%29-950qi.md)
  Modifies a column slice by adding a value to each element.
- [static func -= (inout ColumnSlice<WrappedElement>, WrappedElement)](./minuseq%28_,_%29-1n1gh.md)
  Modifies a column slice by subtracting a value from each element.
- [static func *= (inout ColumnSlice<WrappedElement>, WrappedElement)](./stareq%28_,_%29-i6qs.md)
  Modifies a column slice by multiplying each element by a value.
- [static func /= (inout ColumnSlice<WrappedElement>, WrappedElement)](./opeq%28_,_%29-8pl3f.md)
  Modifies a floating-point column slice by dividing each element by a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/_=(_:_:)-8oi36)*