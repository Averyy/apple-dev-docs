# init(scalars:shape:)

**Framework**: Core ML  
**Kind**: init

Creates a shaped array type from an array of values.

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
init<S>(scalars: S, shape: [Int]) where S : Sequence, Self.Scalar == S.Element
```

## Parameters

- `scalars`: A sequence of values.
- `shape`: An integer array. Each element represents the size of the shaped array’s corresponding dimension.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(scalars:shape:))*