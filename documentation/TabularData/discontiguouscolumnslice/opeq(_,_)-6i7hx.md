# /=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Modifies a floating-point column slice by dividing each element by a value.

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
static func /= (lhs: inout DiscontiguousColumnSlice<WrappedElement>, rhs: WrappedElement) where WrappedElement : FloatingPoint
```

## Parameters

- `lhs`: A column slice.
- `rhs`: A value of the same type as the column’s elements.

## See Also

### Modifying a Column Slice with a Value
- [static func += (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./pluseq%28_,_%29-1mzz0.md)
  Modifies a column slice by adding a value to each element.
- [static func -= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./minuseq%28_,_%29-2yrui.md)
  Modifies a column slice by subtracting a value from each element.
- [static func *= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./stareq%28_,_%29-7gcqc.md)
  Modifies a column slice by multiplying each element by a value.
- [static func /= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./opeq%28_,_%29-1g0yb.md)
  Modifies an integer column slice by dividing each element by a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/_=(_:_:)-6i7hx)*