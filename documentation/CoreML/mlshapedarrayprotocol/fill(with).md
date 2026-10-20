# fill(with:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Fills the array with a value.

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

**Other overloads**:

```swift
mutating func fill<C>(with collection: C) where C : Collection, Self.Scalar == C.Element
```

## Parameters

- `value`: The filling value

## See Also

### Modifying a shaped array type
- [func withUnsafeMutableShapedBufferPointer<R>((inout UnsafeMutableBufferPointer<Self.Scalar>, [Int], [Int]) throws -> R) rethrows -> R](./withunsafemutableshapedbufferpointer%28_%29.md)
  Provides read-write access of the shaped array’s underlying memory to a closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/fill(with:))*