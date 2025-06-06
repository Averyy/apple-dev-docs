# storeBytes(of:toByteOffset:as:)

**Framework**: Swift  
**Kind**: method

Stores the given value’s bytes into raw memory at the specified offset.

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
func storeBytes<T>(of value: T, toByteOffset offset: Int = 0, as type: T.Type)
```

#### Discussion

The type `T` to be stored must be a trivial type. The memory must also be uninitialized, initialized to `T`, or initialized to another trivial type that is layout compatible with `T`.

After calling `storeBytes(of:toByteOffset:as:)`, the memory is initialized to the raw bytes of `value`. If the memory is bound to a type `U` that is layout compatible with `T`, then it contains a value of type `U`. Calling `storeBytes(of:toByteOffset:as:)` does not change the bound type of the memory.

> **Note**: A trivial type can be copied with just a bit-for-bit copy without any indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums.

A trivial type can be copied with just a bit-for-bit copy without any indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums.

If you need to store into memory a copy of a value of a type that isn’t trivial, you cannot use the `storeBytes(of:toByteOffset:as:)` method. Instead, you must know either initialize the memory or, if you know the memory was already bound to `type`, assign to the memory. For example, to replace a value stored in a raw pointer `p`, where `U` is the current type and `T` is the new type, use a typed pointer to access and deinitialize the current value before initializing the memory with a new value:

```swift
let typedPointer = p.bindMemory(to: U.self, capacity: 1)
typedPointer.deinitialize(count: 1)
p.initializeMemory(as: T.self, repeating: newValue, count: 1)
```

## Parameters

- `value`: The value to store as raw bytes.
- `offset`: The offset from this pointer, in bytes.   must be   nonnegative. The default is zero.
- `type`: The type of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/storebytes(of:tobyteoffset:as:)-9mpot)*