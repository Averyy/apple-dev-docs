# init(repeating:shape:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array type that initializes every element to the same value.

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
init(repeating value: Self.Scalar, shape: [Int])
```

## Parameters

- `value`: A scalar value. The initializer assigns every element in the shaped array to `value`.
- `shape`: An integer array. Each element represents the size of the shaped array’s corresponding dimension.

## See Also

### Creating a shaped array type
- [init<S>(scalars: S, shape: [Int])](./init%28scalars,shape%29.md)
  Creates a shaped array type from an array of values.
- [init(identityMatrixOfSize:)](./init%28identitymatrixofsize%29.md)
  Initialize as an identity matrix.
- [init(randomScalarsIn:shape:)](./init%28randomscalarsin,shape%29.md)
  Initialize the shaped array with random scalar values.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], deallocator: Data.Deallocator)](./init%28bytesnocopy,shape,deallocator%29.md)
  Creates a shaped array type from a data pointer.
- [init(bytesNoCopy: UnsafeRawPointer, shape: [Int], strides: [Int], deallocator: Data.Deallocator)](./init%28bytesnocopy,shape,strides,deallocator%29.md)
  Creates a shaped array type from a data pointer with memory strides.
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int]) throws -> Void) rethrows](./init%28unsafeuninitializedshape,initializingwith%29.md)
  Creates a shaped array type from a shape and a closure that initializes its memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(repeating:shape:))*