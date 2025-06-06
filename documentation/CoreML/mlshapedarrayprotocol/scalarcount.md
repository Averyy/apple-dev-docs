# scalarCount

**Framework**: Core ML  
**Kind**: property

The total number of elements in the shaped array type.

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
var scalarCount: Int { get }
```

## See Also

- [var shape: [Int]](mlshapedarrayprotocol/shape.md)
  An integer array in which each element represents the size of the corresponding dimension.
- [var strides: [Int]](mlshapedarrayprotocol/strides.md)
  An integer array in which each element is the number of memory locations that spans the length of the corresponding dimension.
- [var count: Int](mlshapedarrayprotocol/count.md)
  The number of elements in the shaped array’s first dimension.
- [var isScalar: Bool](mlshapedarrayprotocol/isscalar.md)
  A Boolean value that indicates whether the shaped array lacks a shape.
- [var scalar: Self.Scalar?](mlshapedarrayprotocol/scalar-swift.property.md)
  A computed property that returns the first element when the shape isn’t empty, or sets the shaped array’s underlying scalar type.
- [var scalars: [Self.Scalar]](mlshapedarrayprotocol/scalars.md)
  A computed property that generates a linear array that contains every element, or assigns the elements of an array to the shaped array’s elements.
- [func withUnsafeShapedBufferPointer<R>((UnsafeBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R](mlshapedarrayprotocol/withunsafeshapedbufferpointer(_:).md)
  Provides read-only access of the shaped array’s underlying memory to a closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/scalarcount)*