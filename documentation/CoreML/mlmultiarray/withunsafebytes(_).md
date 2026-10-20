# withUnsafeBytes(_:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Calls a given closure with a raw pointer to the multiarray’s storage.

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
func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) rethrows -> R
```

## Parameters

- `body`: A closure with an [`UnsafeRawBufferPointer`](../../Swift/unsaferawbufferpointer.md) parameter that points to the storage for the multiarray. This closure takes the following parameter:

  - **`ptr`**: The pointer to the buffer.

## See Also

### Providing buffer access
- [func withUnsafeBufferPointer<S, R>(ofType: S.Type, (UnsafeBufferPointer<S>) throws -> R) rethrows -> R](./withunsafebufferpointer%28oftype,_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeMutableBufferPointer<S, R>(ofType: S.Type, (UnsafeMutableBufferPointer<S>, [Int]) throws -> R) rethrows -> R](./withunsafemutablebufferpointer%28oftype,_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer, [Int]) throws -> R) rethrows -> R](./withunsafemutablebytes%28_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/withunsafebytes(_:))*