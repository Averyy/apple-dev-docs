# Manual Memory Management

**Framework**: Swift

Allocate and manage memory manually.

## Topics

### First Steps
- [Calling Functions With Pointer Parameters](calling-functions-with-pointer-parameters.md)
  Use implicit pointer casting or bridging when calling functions that takes pointers as parameters.
### Typed Pointers
- [struct UnsafePointer](unsafepointer.md)
  A pointer for accessing data of a specific type.
- [struct UnsafeMutablePointer](unsafemutablepointer.md)
  A pointer for accessing and manipulating data of a specific type.
- [struct UnsafeBufferPointer](unsafebufferpointer.md)
  A nonowning collection interface to a buffer of elements stored contiguously in memory.
- [struct UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
  A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.
### Raw Pointers
- [struct UnsafeRawPointer](unsaferawpointer.md)
  A raw pointer for accessing untyped data.
- [struct UnsafeMutableRawPointer](unsafemutablerawpointer.md)
  A raw pointer for accessing and manipulating untyped data.
- [struct UnsafeRawBufferPointer](unsaferawbufferpointer.md)
  A  nonowning collection interface to the bytes in a region of memory.
- [struct UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
  A mutable nonowning collection interface to the bytes in a region of memory.
### Memory Access
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
- [func withUnsafeTemporaryAllocation<T, R>(of: T.Type, capacity: Int, (UnsafeMutableBufferPointer<T>) throws -> R) rethrows -> R](withunsafetemporaryallocation(of:capacity:_:).md)
  Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [func withUnsafeTemporaryAllocation<R>(byteCount: Int, alignment: Int, (UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](withunsafetemporaryallocation(bytecount:alignment:_:).md)
  Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [func swap<T>(inout T, inout T)](swap(_:_:).md)
  Exchanges the values of the two arguments.
- [func exchange<T>(inout T, with: consuming T) -> T](exchange(_:with:).md)
  Replaces the value of a mutable value with the supplied new value, returning the original.
### Memory Layout
- [enum MemoryLayout](memorylayout.md)
  The memory layout of a type, describing its size, stride, and alignment.
### Reference Counting
- [struct Unmanaged](unmanaged.md)
  A type for propagating an unmanaged object reference.
- [func withExtendedLifetime<T, E, Result>(borrowing T, (borrowing T) throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-4kl68.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [func withExtendedLifetime<T, E, Result>(borrowing T, () throws(E) -> Result) throws(E) -> Result](withextendedlifetime(_:_:)-6mq1.md)
  Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.

## See Also

- [Input and Output](input-and-output.md)
  Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md)
  Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md)
  Generate boilerplate code and perform other compile-time operations.
- [Concurrency](concurrency.md)
  Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md)
  Use key-path expressions to access properties dynamically.
- [Type Casting and Existential Types](type-casting-and-existential-types.md)
  Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md)
  Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/manual-memory-management)*