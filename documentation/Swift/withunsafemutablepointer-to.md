# withUnsafeMutablePointer(to:_:)

**Framework**: Swift  
**Kind**: func

Calls the given closure with a mutable pointer to the given argument.

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
func withUnsafeMutablePointer<T, E, Result>(to value: inout T, _ body: (UnsafeMutablePointer<T>) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, Result : ~Copyable
```

#### Return Value

The return value, if any, of the `body` closure.

#### Discussion

The `withUnsafeMutablePointer(to:_:)` function is useful for calling Objective-C APIs that take in/out parameters (and default-constructible out parameters) by pointer.

The pointer argument to `body` is valid only during the execution of `withUnsafeMutablePointer(to:_:)`. Do not store or return the pointer for later use.

## Parameters

- `value`: An instance to temporarily use via pointer. Note that the    exclusivity rules mean that, like any other   argument,    cannot be directly accessed by other code for the duration of  .   Access must only occur through the pointer argument to   until    returns.
- `body`: A closure that takes a mutable pointer to   as its sole   argument. If the closure has a return value, that value is also used   as the return value of the   function.   The pointer argument is valid only for the duration of the function’s   execution.

## See Also

- [func withUnsafePointer<T, E, Result>(to: inout T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-9fjn6.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafePointer<T, E, Result>(to: borrowing T, (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result](withunsafepointer(to:_:)-35wrn.md)
  Invokes the given closure with a pointer to the given argument.
- [func withUnsafeBytes<T, E, Result>(of: inout T, (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafebytes(of:_:)-5zxtl.md)
  Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeBytes<T, E, Result>(of: borrowing T, (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafebytes(of:_:)-5gesg.md)
  Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [func withUnsafeMutableBytes<T, E, Result>(of: inout T, (UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](withunsafemutablebytes(of:_:).md)
  Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafemutablepointer(to:_:))*