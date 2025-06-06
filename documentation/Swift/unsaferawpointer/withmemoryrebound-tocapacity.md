# withMemoryRebound(to:capacity:_:)

**Framework**: Swift  
**Kind**: method

Executes the given closure while temporarily binding memory to the specified number of instances of type `T`.

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
func withMemoryRebound<T, E, Result>(to type: T.Type, capacity count: Int, _ body: (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, Result : ~Copyable
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

Use this method when you have a pointer to raw memory and you need to access that memory as instances of a given type `T`. Accessing memory as a type `T` requires that the memory be bound to that type. A memory location may only be bound to one type at a time, so accessing the same memory as an unrelated type without first rebinding the memory is undefined.

Any instance of `T` within the re-bound region may be initialized or uninitialized. The memory underlying any individual instance of `T` must have the same initialization state (i.e.  initialized or uninitialized.) Accessing a `T` whose underlying memory is in a mixed initialization state shall be undefined behaviour.

The following example temporarily rebinds a raw memory pointer to `Int64`, then accesses a property on the signed integer.

```swift
let pointer: UnsafeRawPointer = fetchValue()
let isNegative = pointer.withMemoryRebound(
    to: Int64.self, capacity: 1
) {
    return $0.pointee < 0
}
```

After executing `body`, this method rebinds memory back to its original binding state. This can be unbound memory, or bound to a different type.

> **Note**: The region of memory starting at this pointer must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: self) % MemoryLayout<T>.alignment` must equal zero.

The region of memory starting at this pointer must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: self) % MemoryLayout<T>.alignment` must equal zero.

> **Note**: The region of memory starting at this pointer may have been bound to a type. If that is the case, then `T` must be layout compatible with the type to which the memory has been bound. This requirement does not apply if the region of memory has not been bound to any type.

The region of memory starting at this pointer may have been bound to a type. If that is the case, then `T` must be layout compatible with the type to which the memory has been bound. This requirement does not apply if the region of memory has not been bound to any type.

## Parameters

- `type`: The type to temporarily bind the memory referenced by this   pointer. This pointer must be a multiple of this type’s alignment.
- `count`: The number of instances of   in the re-bound region.
- `body`: A closure that takes a typed pointer to the   same memory as this pointer, only bound to type  . The closure’s   pointer argument is valid only for the duration of the closure’s   execution. If   has a return value, that value is also used as   the return value for the   method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawpointer/withmemoryrebound(to:capacity:_:))*