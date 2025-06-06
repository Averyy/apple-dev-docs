# withMemoryRebound(to:_:)

**Framework**: Swift  
**Kind**: method

Executes the given closure while temporarily binding the buffer slice to instances of type `T`.

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
func withMemoryRebound<T, Result, E>(to type: T.Type, _ body: (UnsafeBufferPointer<T>) throws(E) -> Result) throws(E) -> Result where E : Error
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

Use this method when you have a buffer slice to raw memory and you need to access that memory as instances of a given type `T`. Accessing memory as a type `T` requires that the memory be bound to that type. A memory location may only be bound to one type at a time, so accessing the same memory as an unrelated type without first rebinding the memory is undefined.

Any instance of `T` within the re-bound region may be initialized or uninitialized. The memory underlying any individual instance of `T` must have the same initialization state (i.e.  initialized or uninitialized.) Accessing a `T` whose underlying memory is in a mixed initialization state shall be undefined behaviour.

If the byte count of the original buffer slice is not a multiple of the stride of `T`, then the re-bound buffer is shorter than the original buffer.

After executing `body`, this method rebinds memory back to its original binding state. This can be unbound memory, or bound to a different type.

> **Note**: The buffer slice’s start address must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: base.baseAddress+startIndex) % MemoryLayout<T>.alignment` must equal zero.

> **Note**: A raw buffer slice may represent memory that has been bound to a type. If that is the case, then `T` must be layout compatible with the type to which the memory has been bound. This requirement does not apply if the raw buffer represents memory that has not been bound to any type.

## Parameters

- `type`: The type to temporarily bind the memory referenced by this   buffer slice.
- `body`: A closure that takes a typed pointer to the   same memory as this pointer, only bound to type  . The closure’s   pointer argument is valid only for the duration of the closure’s   execution. If   has a return value, that value is also used as   the return value for the   method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/withmemoryrebound(to:_:)-31406)*