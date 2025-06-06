# C Interoperability

**Framework**: Swift

Use imported C types or call C variadic functions.

## Topics

### C and Objective-C Pointers
- [struct OpaquePointer](opaquepointer.md)
  A wrapper around an opaque C pointer.
- [struct AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md)
  A mutable pointer addressing an Objective-C reference that doesn’t own its target.
### C Variadic Functions
- [func withVaList<R>([any CVarArg], (CVaListPointer) -> R) -> R](withvalist(_:_:).md)
  Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [struct CVaListPointer](cvalistpointer.md)
- [protocol CVarArg](cvararg.md)
  A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [func getVaList([any CVarArg]) -> CVaListPointer](getvalist(_:).md)
  Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.
### Pointers to Values
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
### Aliases for Imported C Types
- [typealias CBool](cbool.md)
  The C ‘_Bool’ and C++ ‘bool’ type.
- [typealias CChar](cchar.md)
  The C ‘char’ type.
- [typealias CChar16](cchar16.md)
  The C++11 ‘char16_t’ type, which has UTF-16 encoding.
- [typealias CChar32](cchar32.md)
  The C++11 ‘char32_t’ type, which has UTF-32 encoding.
- [typealias CDouble](cdouble.md)
  The C ‘double’ type.
- [typealias CLongDouble](clongdouble.md)
- [typealias CFloat](cfloat.md)
  The C ‘float’ type.
- [typealias CFloat16](cfloat16.md)
  The C ‘_Float16’ type.
- [typealias CInt](cint.md)
- [typealias CLong](clong.md)
- [typealias CLongLong](clonglong.md)
  The C ‘long long’ type.
- [typealias CShort](cshort.md)
  The C ‘short’ type.
- [typealias CSignedChar](csignedchar.md)
  The C ‘signed char’ type.
- [typealias CUnsignedChar](cunsignedchar.md)
  The C ‘unsigned char’ type.
- [typealias CUnsignedInt](cunsignedint.md)
- [typealias CUnsignedLong](cunsignedlong.md)
- [typealias CUnsignedLongLong](cunsignedlonglong.md)
  The C ‘unsigned long long’ type.
- [typealias CUnsignedShort](cunsignedshort.md)
  The C ‘unsigned short’ type.
- [typealias CWideChar](cwidechar.md)

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
- [Manual Memory Management](manual-memory-management.md)
  Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md)
  Perform casts between types or represent values of any type.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/c-interoperability)*