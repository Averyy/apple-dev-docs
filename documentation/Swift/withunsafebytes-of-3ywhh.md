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
func withUnsafeBytes<T, E, Result>(of value: inout T, _ body: (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, T : ~Escapable, Result : ~Copyable
```

#### Return Value

The return value, if any, of the `body` closure.

#### Discussion

The buffer pointer argument to the `body` closure provides a collection interface to the raw bytes of `value`. The buffer is the size of the instance passed as `value` and does not include any remote storage.

## Parameters

- `value`: An instance to temporarily access through a raw buffer pointer. Note that the `inout` exclusivity rules mean that, like any other `inout` argument, `value` cannot be directly accessed by other code for the duration of `body`. Access must only occur through the pointer argument to `body` until `body` returns.
- `body`: A closure that takes a raw buffer pointer to the bytes of `value` as its sole argument. If the closure has a return value, that value is also used as the return value of the `withUnsafeBytes(of:_:)` function. The buffer pointer argument is valid only for the duration of the closure’s execution. It is undefined behavior to attempt to mutate through the pointer by conversion to `UnsafeMutableRawBufferPointer` or any other mutable pointer type. If you want to mutate a value by writing through a pointer, use `withUnsafeMutableBytes(of:_:)` instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafebytes(of:_:)-3ywhh)*