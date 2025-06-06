# withUnsafeBytes(of:_:)

**Framework**: Swift  
**Kind**: func

Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.

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
func withUnsafeBytes<T, E, Result>(of value: borrowing T, _ body: (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, Result : ~Copyable
```

#### Return Value

The return value, if any, of the `body` closure.

#### Discussion

The buffer pointer argument to the `body` closure provides a collection interface to the raw bytes of `value`. The buffer is the size of the instance passed as `value` and does not include any remote storage.

## Parameters

- `value`: An instance to temporarily access through a raw buffer pointer.
- `body`: A closure that takes a raw buffer pointer to the bytes of    as its sole argument. If the closure has a return value, that value is   also used as the return value of the    function. The buffer pointer argument is valid only for the duration   of the closure’s execution. It is undefined behavior to attempt to   mutate through the pointer by conversion to    or any other mutable pointer type.   If you want to mutate a value by writing through a pointer, use    instead.

## See Also

- [func withUnsafePointer<T, E, Result>(to: inout T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-9fjn6.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafePointer<T, E, Result>(to: borrowing T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-35wrn.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafeMutablePointer<T, E, Result>(to: inout T, (UnsafeMutablePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafemutablepointer(to:_:).md)
  Calls the given closure with a mutable pointer to the given argument.
- [func withUnsafeBytes<T, E, Result>(of: inout T, (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafebytes(of:_:)-5zxtl.md)
  Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeMutableBytes<T, E, Result>(of: inout T, (UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafemutablebytes(of:_:).md)
  Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafebytes(of:_:)-5gesg)*