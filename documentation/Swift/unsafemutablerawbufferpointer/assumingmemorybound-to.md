# assumingMemoryBound(to:)

**Framework**: Swift  
**Kind**: method

Returns a typed buffer to the memory referenced by this buffer, assuming that the memory is already bound to the specified type.

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
func assumingMemoryBound<T>(to: T.Type) -> UnsafeMutableBufferPointer<T> where T : ~Copyable
```

#### Return Value

A typed pointer to the same memory as this raw pointer.

#### Discussion

Use this method when you have a raw buffer to memory that has already been bound to the specified type. The memory starting at this pointer must be bound to the type `T`. Accessing memory through the returned pointer is undefined if the memory has not been bound to `T`. To bind memory to `T`, use `bindMemory(to:capacity:)` instead of this method.

> **Note**: The buffer’s base address must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: self.baseAddress) % MemoryLayout<T>.alignment` must equal zero.

The buffer’s base address must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: self.baseAddress) % MemoryLayout<T>.alignment` must equal zero.

## Parameters

- `to`: The type   that the memory has already been bound to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/assumingmemorybound(to:))*