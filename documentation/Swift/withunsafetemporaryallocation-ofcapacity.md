# withUnsafeTemporaryAllocation(of:capacity:_:)

**Framework**: Swift  
**Kind**: func

Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.

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
func withUnsafeTemporaryAllocation<T, R>(of type: T.Type, capacity: Int, _ body: (UnsafeMutableBufferPointer<T>) throws -> R) rethrows -> R where T : ~Copyable, R : ~Copyable
```

#### Return Value

Whatever is returned by `body`.

#### Discussion

> **Note**: Whatever is thrown by `body`.

This function is useful for cheaply allocating storage for a sequence of values for a brief duration. Storage may be allocated on the heap or on the stack, depending on the required size and alignment.

When `body` is called, the contents of the buffer pointer passed to it are in an unspecified, uninitialized state. `body` is responsible for initializing the buffer pointer before it is used  for deinitializing it before returning, but deallocation is automatic.

The implementation may allocate a larger buffer pointer than is strictly necessary to contain `capacity` values of type `type`. The behavior of a program that attempts to access any such additional storage is undefined.

The buffer pointer passed to `body` (as well as any pointers to elements in the buffer) must not escape. It will be deallocated when `body` returns and cannot be used afterward.

## Parameters

- `type`: The type of the elements in the buffer being temporarily   allocated.
- `capacity`: The capacity of the buffer pointer being temporarily   allocated.
- `body`: A closure to invoke and to which the allocated buffer pointer   should be passed.

## See Also

- [func withUnsafePointer<T, E, Result>(to: inout T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-9fjn6.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafePointer<T, E, Result>(to: borrowing T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-35wrn.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafeMutablePointer<T, E, Result>(to: inout T, (UnsafeMutablePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafemutablepointer(to:_:).md)
  Calls the given closure with a mutable pointer to the given argument.
- [func withUnsafeBytes<T, E, Result>(of: inout T, (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafebytes(of:_:)-5zxtl.md)
  Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeBytes<T, E, Result>(of: borrowing T, (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafebytes(of:_:)-5gesg.md)
  Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeMutableBytes<T, E, Result>(of: inout T, (UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafemutablebytes(of:_:).md)
  Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeTemporaryAllocation<R>(byteCount: Int, alignment: Int, (UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](withunsafetemporaryallocation(bytecount:alignment:_:).md)
  Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [func swap<T>(inout T, inout T)](swap(_:_:).md)
  Exchanges the values of the two arguments.
- [func exchange<T>(inout T, with: consuming T) -> T](exchange(_:with:).md)
  Replaces the value of a mutable value with the supplied new value, returning the original.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafetemporaryallocation(of:capacity:_:))*