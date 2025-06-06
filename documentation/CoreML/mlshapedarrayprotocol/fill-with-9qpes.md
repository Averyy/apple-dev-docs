# fill(with:)

**Framework**: Core ML  
**Kind**: method

Assigns the shaped array’s elements to a value.

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
mutating func fill(with value: Self.Scalar)
```

## Parameters

- `value`: A scalar value.

## See Also

- [func fill<C>(with: C)](mlshapedarrayprotocol/fill(with:)-6a5k1.md)
  Assigns the shaped array’s elements to the elements in a collection, repeatedly, if necessary.
- [func withUnsafeMutableShapedBufferPointer<R>((inout UnsafeMutableBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R](mlshapedarrayprotocol/withunsafemutableshapedbufferpointer(_:).md)
  Provides read-write access of the shaped array’s underlying memory to a closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/fill(with:)-9qpes)*