# withUnsafeMutableShapedBufferPointer(_:)

**Framework**: Core ML  
**Kind**: method  
**Required**: Yes

Provides read-write access of the shaped array’s underlying memory to a closure.

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
mutating func withUnsafeMutableShapedBufferPointer<R>(_ body: (inout UnsafeMutableBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R
```

#### Discussion

The method returns the value your closure returns, if applicable.

## Parameters

- `body`: A closure that accesses a shaped array’s underlying memory.

## See Also

- [func fill(with:)](mlshapedarrayprotocol/fill(with:).md)
  Fills the array with a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/withunsafemutableshapedbufferpointer(_:))*