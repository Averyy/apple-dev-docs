# MLShapedArrayRangeExpression

**Framework**: Core ML  
**Kind**: protocol

An interface for a range expression, which you typically use with subscripts of shaped array types.

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
protocol MLShapedArrayRangeExpression
```

## Topics

### Generating relative ranges
- [func relative(toShapedArrayAxis: Range<Int>) -> Range<Int>](mlshapedarrayrangeexpression/relative(toshapedarrayaxis:).md)
  Returns the range of indices the range expression describes within a collection.

## See Also

- [associatedtype Scalar : MLShapedArrayScalar](mlshapedarrayprotocol/scalar-swift.associatedtype.md)
  Represents the underlying scalar type of the shaped array type.
- [struct MLShapedArraySlice](mlshapedarrayslice.md)
  A multidimensional subset of elements from a shaped array type.
- [protocol MLShapedArrayScalar](mlshapedarrayscalar.md)
  A type that associates a scalar with a shaped array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayrangeexpression)*