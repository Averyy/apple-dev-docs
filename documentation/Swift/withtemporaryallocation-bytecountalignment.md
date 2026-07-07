# withTemporaryAllocation(byteCount:alignment:_:)

**Framework**: Swift  
**Kind**: func

Provides scoped access to an output raw span with the specified byte count and alignment.

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
func withTemporaryAllocation<R, E>(byteCount: Int, alignment: Int, _ body: @_lifetime(0: copy 0) (inout OutputRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Return Value

Whatever is returned by `body`.

#### Discussion

This function is useful for cheaply allocating raw storage for a brief duration. Storage may be allocated on the heap or on the stack, depending on the required size and alignment.

When `body` is called, it is passed an empty `OutputRawSpan`. `body` may append bytes to the output raw span. After `body` returns, deallocation is automatic.

> **Note**: Whatever is thrown by `body`.

## Parameters

- `byteCount`: The number of bytes to temporarily allocate. `byteCount` must not be negative.
- `alignment`: The alignment of the new, temporary region of allocated memory, in bytes. `alignment` must be a whole power of 2.
- `body`: A closure to invoke and to which the allocated output raw span should be passed.

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
- [func withTemporaryAllocation<T, R, E>(of: T.Type, capacity: Int, (inout OutputSpan<T>) throws(E) -> R) throws(E) -> R](withtemporaryallocation(of:capacity:_:).md)
  Provides scoped access to an output span of the specified type and capacity.
- [func withUnsafeTemporaryAllocation<T, R, E>(of: T.Type, capacity: Int, (UnsafeMutableBufferPointer<T>) throws(E) -> R) throws(E) -> R](withunsafetemporaryallocation(of:capacity:_:).md)
  Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [func withUnsafeTemporaryAllocation<R, E>(byteCount: Int, alignment: Int, (UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](withunsafetemporaryallocation(bytecount:alignment:_:).md)
  Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [func swap<T>(inout T, inout T)](swap(_:_:).md)
  Exchanges the values of the two arguments.
- [func exchange<T>(inout T, with: consuming T) -> T](exchange(_:with:).md)
  Replaces the value of a mutable value with the supplied new value, returning the original.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtemporaryallocation(bytecount:alignment:_:))*