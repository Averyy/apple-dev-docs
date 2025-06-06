# exchange(_:with:)

**Framework**: Swift  
**Kind**: func

Replaces the value of a mutable value with the supplied new value, returning the original.

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
func exchange<T>(_ item: inout T, with newValue: consuming T) -> T where T : ~Copyable
```

#### Return Value

The original value of `item`.

## Parameters

- `item`: A mutable binding.
- `newValue`: The new value of  .

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
- [func withUnsafeTemporaryAllocation<T, R>(of: T.Type, capacity: Int, (UnsafeMutableBufferPointer<T>) throws -> R) rethrows -> R](withunsafetemporaryallocation(of:capacity:_:).md)
  Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [func withUnsafeTemporaryAllocation<R>(byteCount: Int, alignment: Int, (UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](withunsafetemporaryallocation(bytecount:alignment:_:).md)
  Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [func swap<T>(inout T, inout T)](swap(_:_:).md)
  Exchanges the values of the two arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/exchange(_:with:))*