# withUnsafeBufferPointer(_:)

**Framework**: Swift  
**Kind**: method

Calls a closure with a pointer to the array’s contiguous storage.

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
func withUnsafeBufferPointer<R, E>(_ body: (UnsafeBufferPointer<Element>) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

Often, the optimizer can eliminate bounds checks within an array algorithm, but when that fails, invoking the same algorithm on the buffer pointer passed into your closure lets you trade safety for speed.

The following example shows how you can iterate over the contents of the buffer pointer:

```swift
let numbers = [1, 2, 3, 4, 5]
let sum = numbers.withUnsafeBufferPointer { buffer -> Int in
    var result = 0
    for i in stride(from: buffer.startIndex, to: buffer.endIndex, by: 2) {
        result += buffer[i]
    }
    return result
}
// 'sum' == 9
```

The pointer passed as an argument to `body` is valid only during the execution of `withUnsafeBufferPointer(_:)`. Do not store or return the pointer for later use.

## Parameters

- `body`: A closure with an   parameter that   points to the contiguous storage for the array.  If no such storage exists, it is created. If    has a return value, that value is also used as the return value   for the   method. The pointer argument is   valid only for the duration of the method’s execution.

## See Also

- [func withUnsafeMutableBufferPointer<R, E>((inout UnsafeMutableBufferPointer<Element>) throws(E) -> R) throws(E) -> R](array/withunsafemutablebufferpointer(_:).md)
  Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](array/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](array/withunsafemutablebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/withunsafebufferpointer(_:))*