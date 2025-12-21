# MLShapedArrayScalar

**Framework**: Core ML  
**Kind**: protocol

A type that associates a scalar with a shaped array.

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
protocol MLShapedArrayScalar
```

## Topics

### Determining the underlying type
- [static var multiArrayDataType: MLMultiArrayDataType](mlshapedarrayscalar/multiarraydatatype.md)
  The shaped array’s scalar type as a multiarray data type.

## See Also

- [associatedtype Scalar : MLShapedArrayScalar](mlshapedarrayprotocol/scalar-swift.associatedtype.md)
  Represents the underlying scalar type of the shaped array type.
- [struct MLShapedArraySlice](mlshapedarrayslice.md)
  A multidimensional subset of elements from a shaped array type.
- [protocol MLShapedArrayRangeExpression](mlshapedarrayrangeexpression.md)
  An interface for a range expression, which you typically use with subscripts of shaped array types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayscalar)*