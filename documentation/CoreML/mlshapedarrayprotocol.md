# MLShapedArrayProtocol

**Framework**: Core ML  
**Kind**: protocol

An interface that defines a shaped array type.

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
protocol MLShapedArrayProtocol<Scalar> : ExpressibleByArrayLiteral, MutableCollection, RandomAccessCollection where Self.Index == Int
```

## Topics

### Creating a Shaped Array Type
- [init<S>(scalars: S, shape: [Int])](mlshapedarrayprotocol/init(scalars:shape:).md)
  Creates a shaped array type from an array of values.
- [init(repeating: Self.Scalar, shape: [Int])](mlshapedarrayprotocol/init(repeating:shape:).md)
  Creates a shaped array type that initializes every element to the same value.
- [init(identityMatrixOfSize: Int)](mlshapedarrayprotocol/init(identitymatrixofsize:)-77y0e.md)
  Creates a shaped array type that’s an identity matrix of integers.
- [init(randomScalarsIn: Range<Self.Scalar>, shape: [Int])](mlshapedarrayprotocol/init(randomscalarsin:shape:)-99fnn.md)
  Creates a shaped array type that initializes the elements to random integer values within a range.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], deallocator: Data.Deallocator)](mlshapedarrayprotocol/init(bytesnocopy:shape:deallocator:).md)
  Creates a shaped array type from a data pointer.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], strides: [Int], deallocator: Data.Deallocator)](mlshapedarrayprotocol/init(bytesnocopy:shape:strides:deallocator:).md)
  Creates a shaped array type from a data pointer with memory strides.
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int]) throws -> Void) rethrows](mlshapedarrayprotocol/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array type from a shape and a closure that initializes its memory.
### Creating a Shaped Array Type from Another Type
- [init(MLMultiArray)](mlshapedarrayprotocol/init(_:).md)
  Creates a shaped array type from a multiarray.
- [init(converting: MLMultiArray)](mlshapedarrayprotocol/init(converting:)-3d2eu.md)
  Creates a shaped array type by converting a multiarray.
- [init<T>(converting: T)](mlshapedarrayprotocol/init(converting:)-701ib.md)
  Creates a shaped array type by converting another shaped array type.
### Inspecting a Shaped Array Type
- [var shape: [Int]](mlshapedarrayprotocol/shape.md)
  An integer array in which each element represents the size of the corresponding dimension.
- [var strides: [Int]](mlshapedarrayprotocol/strides.md)
  An integer array in which each element is the number of memory locations that spans the length of the corresponding dimension.
- [var count: Int](mlshapedarrayprotocol/count.md)
  The number of elements in the shaped array’s first dimension.
- [var isScalar: Bool](mlshapedarrayprotocol/isscalar.md)
  A Boolean value that indicates whether the shaped array lacks a shape.
- [var scalarCount: Int](mlshapedarrayprotocol/scalarcount.md)
  The total number of elements in the shaped array type.
- [var scalar: Self.Scalar?](mlshapedarrayprotocol/scalar-swift.property.md)
  A computed property that returns the first element when the shape isn’t empty, or sets the shaped array’s underlying scalar type.
- [var scalars: [Self.Scalar]](mlshapedarrayprotocol/scalars.md)
  A computed property that generates a linear array that contains every element, or assigns the elements of an array to the shaped array’s elements.
- [func withUnsafeShapedBufferPointer<R>((UnsafeBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R](mlshapedarrayprotocol/withunsafeshapedbufferpointer(_:).md)
  Provides read-only access of the shaped array’s underlying memory to a closure.
### Accessing Elements
- [subscript<C>(scalarAt _: C) -> Self.Scalar](mlshapedarrayprotocol/subscript(scalarat:).md)
  Accesses an element and a multidimensional location.
- [subscript<C>(C) -> MLShapedArraySlice<Self.Scalar>](mlshapedarrayprotocol/subscript(_:)-zfw5.md)
  Accesses a slice using a collection of integers, in which each element is an index in the corresponding dimension.
- [subscript<C>(C) -> MLShapedArraySlice<Self.Scalar>](mlshapedarrayprotocol/subscript(_:)-1q1sr.md)
  Accesses a slice using a collection of integer ranges, in which each element is a range in the corresponding dimension.
### Modifying a Shaped Array Type
- [func fill(with: Self.Scalar)](mlshapedarrayprotocol/fill(with:)-9qpes.md)
  Assigns the shaped array’s elements to a value.
- [func fill<C>(with: C)](mlshapedarrayprotocol/fill(with:)-6a5k1.md)
  Assigns the shaped array’s elements to the elements in a collection, repeatedly, if necessary.
- [func withUnsafeMutableShapedBufferPointer<R>((inout UnsafeMutableBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R](mlshapedarrayprotocol/withunsafemutableshapedbufferpointer(_:).md)
  Provides read-write access of the shaped array’s underlying memory to a closure.
### Supporting Types
- [associatedtype Scalar : MLShapedArrayScalar](mlshapedarrayprotocol/scalar-swift.associatedtype.md)
  Represents the underlying scalar type of the shaped array type.
- [struct MLShapedArraySlice](mlshapedarrayslice.md)
  A multidimensional subset of elements from a shaped array type.
- [protocol MLShapedArrayScalar](mlshapedarrayscalar.md)
  A type that associates a scalar with a shaped array.
- [protocol MLShapedArrayRangeExpression](mlshapedarrayrangeexpression.md)
  An interface for a range expression, which you typically use with subscripts of shaped array types.
### Initializers
- [init(identityMatrixOfSize: Int)](mlshapedarrayprotocol/init(identitymatrixofsize:)-1xx88.md)
  Initialize as an identity matrix.
- [init(randomScalarsIn: Range<Self.Scalar>, shape: [Int])](mlshapedarrayprotocol/init(randomscalarsin:shape:)-4c8k1.md)
  Initialize the shaped array with random scalar values.

## Relationships

### Inherits From
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)
### Conforming Types
- [MLShapedArray](mlshapedarray.md)
- [MLShapedArraySlice](mlshapedarrayslice.md)

## See Also

- [enum MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [struct MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.
- [class MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.
- [class MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol)*