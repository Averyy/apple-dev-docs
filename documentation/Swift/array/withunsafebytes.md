# withUnsafeBytes(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The array’s `Element` type must be a , which can be copied with just a bit-for-bit copy without any indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references are trivial, as are imported C structs and enums.

The following example copies the bytes of the `numbers` array into a buffer of `UInt8`:

```swift
var numbers: [Int32] = [1, 2, 3]
var byteBuffer: [UInt8] = []
numbers.withUnsafeBytes {
    byteBuffer.append(contentsOf: $0)
}
// byteBuffer == [1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0]
```

> **Note**: This example shows the behavior on a little-endian platform.

This example shows the behavior on a little-endian platform.

## Parameters

- `body`: A closure with an   parameter   that points to the contiguous storage for the array.   If no such storage exists, it is created. If   has a return value, that value is also   used as the return value for the   method. The   argument is valid only for the duration of the closure’s execution.

## See Also

- [func withUnsafeBufferPointer<R, E>((UnsafeBufferPointer<Element>) throws(E) -> R) throws(E) -> R](array/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the array’s contiguous storage.
- [func withUnsafeMutableBufferPointer<R, E>((inout UnsafeMutableBufferPointer<Element>) throws(E) -> R) throws(E) -> R](array/withunsafemutablebufferpointer(_:).md)
  Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](array/withunsafemutablebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/withunsafebytes(_:))*