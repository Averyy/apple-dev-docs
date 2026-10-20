# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

A slice of the shaped array for the selected leading axes.

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
subscript<C>(indices: C) -> MLShapedArraySlice<Self.Scalar> where C : Collection, C.Element == Int { get set }
```

**Other overloads**:

```swift
subscript<C>(sliceRanges: C) -> MLShapedArraySlice<Self.Scalar> where C : Collection, C.Element == Range<Int> { get set }
```

#### Overview

The slice has a rank of `self.rank - indices.count`. For example, given a shaped array `m` with the shape being `3 x 3`, `m[[1]]` returns a slice of shape `[3]` with the contents labeld as `x` below.

```
 O  O  O
 x  x  x
 O  O  O
```

## Parameters

- `indices`: The indices to slice the array.

## Default Implementations

### MLShapedArrayProtocol Implementations
- [subscript(Range<Int>) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-23n4b.md)
  A slice of the shaped array for the specified ranges.
- [subscript(Int...) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-2cxk1.md)
  A slice of the shaped array for the selected leading axes.
- [subscript(any MLShapedArrayRangeExpression...) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-2hc37.md)
  A slice of the shaped array for the specified ranges.
- [subscript((UnboundedRange_) -> Void) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-3ao6n.md)
- [subscript(any MLShapedArrayRangeExpression) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-5r9r3.md)
  A slice of the shaped array for the specified ranges.
- [subscript<C>(C) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-70104.md)
  A slice of the shaped array for the specified ranges.
- [subscript(Int) -> MLShapedArraySlice<Self.Scalar>](./subscript%28_%29-79cx4.md)

## See Also

### Accessing elements
- [subscript<C>(scalarAt _: C) -> Self.Scalar](./subscript%28scalarat%29.md)
  Accesses an element and a multidimensional location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(_:))*