# withUnsafeMutableBufferPointer(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure with a pointer to the array’s mutable contiguous storage.

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
mutating func withUnsafeMutableBufferPointer<R, E>(_ body: (inout UnsafeMutableBufferPointer<Element>) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

Often, the optimizer can eliminate bounds checks within an array algorithm, but when that fails, invoking the same algorithm on the buffer pointer passed into your closure lets you trade safety for speed.

The following example shows how modifying the contents of the `UnsafeMutableBufferPointer` argument to `body` alters the contents of the array:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.withUnsafeMutableBufferPointer { buffer in
    for i in stride(from: buffer.startIndex, to: buffer.endIndex - 1, by: 2) {
        buffer.swapAt(i, i + 1)
    }
}
print(numbers)
// Prints "[2, 1, 4, 3, 5]"
```

The pointer passed as an argument to `body` is valid only during the execution of `withUnsafeMutableBufferPointer(_:)`. Do not store or return the pointer for later use.

> ⚠️ **Warning**: Do not rely on anything about the array that is the target of this method during execution of the `body` closure; it might not appear to have its correct value. Instead, use only the `UnsafeMutableBufferPointer` argument to `body`.

Do not rely on anything about the array that is the target of this method during execution of the `body` closure; it might not appear to have its correct value. Instead, use only the `UnsafeMutableBufferPointer` argument to `body`.

## Parameters

- `body`: A closure with an    parameter that points to the contiguous storage for the array.   If no such storage exists, it is created. If   has a return value, that value is also   used as the return value for the    method. The pointer argument is valid only for the duration of the   method’s execution.

## See Also

- [func withUnsafeBufferPointer<R, E>((UnsafeBufferPointer<Element>) throws(E) -> R) throws(E) -> R](array/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the array’s contiguous storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](array/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](array/withunsafemutablebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/withunsafemutablebufferpointer(_:))*