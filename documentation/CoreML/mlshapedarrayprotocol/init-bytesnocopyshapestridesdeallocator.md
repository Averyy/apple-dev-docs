# init(bytesNoCopy:shape:strides:deallocator:)

**Framework**: Core ML  
**Kind**: init  
**Required**: Yes

Creates a shaped array type from a data pointer with memory strides.

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
init(bytesNoCopy bytes: UnsafeRawPointer, shape: [Int], strides: [Int], deallocator: Data.Deallocator)
```

## Parameters

- `bytes`: An unsafe raw pointer to the data.
- `shape`: An integer array. Each element represents the size of the shaped array’s corresponding dimension.
- `strides`: An integer array. Each element represents the number of memory locations that span the shaped array’s corresponding dimension.
- `deallocator`: A  .

## See Also

- [init<S>(scalars: S, shape: [Int])](mlshapedarrayprotocol/init(scalars:shape:).md)
  Creates a shaped array type from an array of values.
- [init(repeating: Self.Scalar, shape: [Int])](mlshapedarrayprotocol/init(repeating:shape:).md)
  Creates a shaped array type that initializes every element to the same value.
- [init(identityMatrixOfSize:)](mlshapedarrayprotocol/init(identitymatrixofsize:).md)
  Initialize as an identity matrix.
- [init(randomScalarsIn:shape:)](mlshapedarrayprotocol/init(randomscalarsin:shape:).md)
  Initialize the shaped array with random scalar values.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], deallocator: Data.Deallocator)](mlshapedarrayprotocol/init(bytesnocopy:shape:deallocator:).md)
  Creates a shaped array type from a data pointer.
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int]) throws -> Void) rethrows](mlshapedarrayprotocol/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array type from a shape and a closure that initializes its memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(bytesnocopy:shape:strides:deallocator:))*