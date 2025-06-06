# init(unsafeUninitializedShape:scalarType:initializingWith:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor with the specified shape, then calls the given closure with a buffer covering the tensor’s uninitialized memory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(unsafeUninitializedShape shape: [Int], scalarType: any MLTensorScalar.Type, initializingWith initializer: (UnsafeMutableRawBufferPointer) throws -> Void) rethrows
```

## Parameters

- `shape`: The dimensions of the tensor.
- `scalarType`: The scalar type.
- `initializer`: A closure which will be called to initialize the underlying memory of the tensor. Scalars expected to be   stored contiguously in first-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(unsafeuninitializedshape:scalartype:initializingwith:))*