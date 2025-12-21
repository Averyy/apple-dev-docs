# init(identityMatrixOfSize:)

**Framework**: Core ML  
**Kind**: init

Initialize as an identity matrix.

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
init(identityMatrixOfSize size: Int)
```

#### Discussion

The initializer creates a shaped array of shape size x size where the contents are zeros except array[scalarAt: x, x], which are ones.

## Parameters

- `size`: The size (order) of the matrix

## See Also

- [init<S>(scalars: S, shape: [Int])](mlshapedarrayprotocol/init(scalars:shape:).md)
  Creates a shaped array type from an array of values.
- [init(repeating: Self.Scalar, shape: [Int])](mlshapedarrayprotocol/init(repeating:shape:).md)
  Creates a shaped array type that initializes every element to the same value.
- [init(randomScalarsIn:shape:)](mlshapedarrayprotocol/init(randomscalarsin:shape:).md)
  Initialize the shaped array with random scalar values.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], deallocator: Data.Deallocator)](mlshapedarrayprotocol/init(bytesnocopy:shape:deallocator:).md)
  Creates a shaped array type from a data pointer.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], strides: [Int], deallocator: Data.Deallocator)](mlshapedarrayprotocol/init(bytesnocopy:shape:strides:deallocator:).md)
  Creates a shaped array type from a data pointer with memory strides.
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int]) throws -> Void) rethrows](mlshapedarrayprotocol/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array type from a shape and a closure that initializes its memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(identitymatrixofsize:))*