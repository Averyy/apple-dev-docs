# withUnsafeMutableBytes(_:)

**Framework**: Core ML  
**Kind**: method

Calls a given closure with a raw pointer to the multiarray’s mutable storage.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
func withUnsafeMutableBytes<R>(_ body: (UnsafeMutableRawBufferPointer, [Int]) throws -> R) rethrows -> R
```

#### Discussion

The buffer contains a collection of `int32`, `float16`, `float32`, or `float64` values, depending on the multiarray’s data type. It may not store these scalar values contiguously; use `strides` to get the buffer layout.

## Parameters

- `body`: A closure with an   parameter that points to the storage for the multiarray and its strides. This closure takes the following parameters:

## See Also

- [func withUnsafeBufferPointer<S, R>(ofType: S.Type, (UnsafeBufferPointer<S>) throws -> R) rethrows -> R](mlmultiarray/withunsafebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](mlmultiarray/withunsafebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeMutableBufferPointer<S, R>(ofType: S.Type, (UnsafeMutableBufferPointer<S>, [Int]) throws -> R) rethrows -> R](mlmultiarray/withunsafemutablebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/withunsafemutablebytes(_:))*