# strides

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An integer array in which each element is the number of memory locations that spans the length of the corresponding dimension.

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
var strides: [Int] { get }
```

## See Also

### Inspecting a shaped array type
- [var shape: [Int]](./shape.md)
  An integer array in which each element represents the size of the corresponding dimension.
- [var count: Int](./count.md)
  The number of elements in the shaped array’s first dimension.
- [var isScalar: Bool](./isscalar.md)
  A Boolean value that indicates whether the shaped array lacks a shape.
- [var scalarCount: Int](./scalarcount.md)
  The total number of elements in the shaped array type.
- [var scalar: Self.Scalar?](./scalar-swift.property.md)
  A computed property that returns the first element when the shape isn’t empty, or sets the shaped array’s underlying scalar type.
- [var scalars: [Self.Scalar]](./scalars.md)
  A computed property that generates a linear array that contains every element, or assigns the elements of an array to the shaped array’s elements.
- [func withUnsafeShapedBufferPointer<R>((UnsafeBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R](./withunsafeshapedbufferpointer%28_%29.md)
  Provides read-only access of the shaped array’s underlying memory to a closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/strides)*