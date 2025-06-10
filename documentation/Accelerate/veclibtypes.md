# vecLibTypes

**Framework**: Accelerate

Create and work with 128-bit vector data types.

#### Overview

The vecLibTypes.h header file defines a set of vector data types (`vFloat`, `vUInt32`, etc.), which represent 128-bit vectors containing values of type `float`, `UInt32`, etc. The vBasicOps.h and vfp.h headers make use of these types.

The type names all begin with the letter “v,” followed by a mnemonic for the scalar data type used for elements of the vector. For example, `vUInt32`, `vSInt16`, `vFloat`, etc.

## Topics

### Type Aliases
- [typealias la_attribute_t](la_attribute_t.md)
- [typealias la_count_t](la_count_t.md)
- [typealias la_deallocator_t](la_deallocator_t.md)
- [typealias la_hint_t](la_hint_t.md)
- [typealias la_index_t](la_index_t.md)
- [typealias la_norm_t](la_norm_t.md)
- [typealias la_object_t](la_object_t.md)
- [typealias la_scalar_type_t](la_scalar_type_t.md)
- [typealias la_status_t](la_status_t.md)
- [protocol OS_la_object](os_la_object.md)
### vecLibTypes
- [typealias vUInt8](vuint8.md)
  A 128-bit vector packed with `unsigned char` values.
- [typealias vSInt8](vsint8.md)
  A 128-bit vector packed with `signed char` values.
- [typealias vUInt16](vuint16.md)
  A 128-bit vector packed with `unsigned short` values.
- [typealias vSInt16](vsint16.md)
  A 128-bit vector packed with `signed short` values.
- [typealias vUInt32](vuint32.md)
  A 128-bit vector packed with `unsigned int` values.
- [typealias vSInt32](vsint32.md)
  A 128-bit vector packed with `signed int` values.
- [typealias vUInt64](vuint64.md)
  A 128-bit vector packed with `uint64_t` values.
- [typealias vSInt64](vsint64.md)
  A 128-bit vector packed with `int64_t` values.
- [typealias vFloat](vfloat.md)
  A 128-bit vector packed with `float` values.
- [typealias vDouble](vdouble.md)
  A 128-bit vector packed with `double` values.
- [typealias vBool32](vbool32.md)
  A 128-bit vector packed with `bool int` values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/veclibtypes)*