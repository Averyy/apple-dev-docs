# withTemporaryAllocation(of:capacity:_:)

**Framework**: Swift  
**Kind**: func

Provides scoped access to an output span of the specified type and capacity.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
func withTemporaryAllocation<T, R, E>(of type: T.Type, capacity: Int, _ body: @_lifetime(0: copy 0) (inout OutputSpan<T>) throws(E) -> R) throws(E) -> R where E : Error, T : ~Copyable, R : ~Copyable
```

#### Return Value

Whatever is returned by `body`.

#### Discussion

This function is useful for cheaply allocating storage for a sequence of values for a brief duration. Storage may be allocated on the heap or on the stack, depending on the required size and alignment.

When `body` is called, it is passed an empty `OutputSpan`. `body` may append or initialize elements in the output span. Any elements that have been initialized when `body` returns are deinitialized automatically, and deallocation is also automatic.

> **Note**: Whatever is thrown by `body`.

## Parameters

- `type`: The type of the elements in the buffer being temporarily allocated.
- `capacity`: The capacity of the output span being temporarily allocated.
- `body`: A closure to invoke and to which the allocated output span should be passed.

## See Also

- [func withUnsafePointer<T, E, Result>(to: inout T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-9fjn6.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafePointer<T, E, Result>(to: borrowing T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-35wrn.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafeMutablePointer<T, E, Result>(to: inout T, (UnsafeMutablePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafemutablepointer(to:_:).md)
  Calls the given closure with a mutable pointer to the given argument.
- [func withUnsafeBytes<T, E, Result>(of: inout T, (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafebytes(of:_:)-3ywhh.md)
  Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeMutableBytes<T, E, Result>(of: inout T, (UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafemutablebytes(of:_:).md)
  Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
- [func withTemporaryAllocation<R, E>(byteCount: Int, alignment: Int, (inout OutputRawSpan) throws(E) -> R) throws(E) -> R](withtemporaryallocation(bytecount:alignment:_:).md)
  Provides scoped access to an output raw span with the specified byte count and alignment.
- [func withUnsafeTemporaryAllocation<T, R, E>(of: T.Type, capacity: Int, (UnsafeMutableBufferPointer<T>) throws(E) -> R) throws(E) -> R](withunsafetemporaryallocation(of:capacity:_:).md)
  Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [func withUnsafeTemporaryAllocation<R, E>(byteCount: Int, alignment: Int, (UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](withunsafetemporaryallocation(bytecount:alignment:_:).md)
  Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [func swap<T>(inout T, inout T)](swap(_:_:).md)
  Exchanges the values of the two arguments.
- [func exchange<T>(inout T, with: consuming T) -> T](exchange(_:with:).md)
  Replaces the value of a mutable value with the supplied new value, returning the original.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtemporaryallocation(of:capacity:_:))*