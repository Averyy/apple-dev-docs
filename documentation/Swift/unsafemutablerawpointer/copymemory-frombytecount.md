# copyMemory(from:byteCount:)

**Framework**: Swift  
**Kind**: method

Copies the specified number of bytes from the given raw pointer’s memory into this pointer’s memory.

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
func copyMemory(from source: UnsafeRawPointer, byteCount: Int)
```

#### Discussion

If the `byteCount` bytes of memory referenced by this pointer are bound to a type `T`, then `T` must be a trivial type, this pointer and `source` must be properly aligned for accessing `T`, and `byteCount` must be a multiple of `MemoryLayout<T>.stride`.

The memory in the region `source..<(source + byteCount)` may overlap with the memory referenced by this pointer.

After calling `copyMemory(from:byteCount:)`, the `byteCount` bytes of memory referenced by this pointer are initialized to raw bytes. If the memory is bound to type `T`, then it contains values of type `T`.

## Parameters

- `source`: A pointer to the memory to copy bytes from. The memory in the   region   must be initialized to a   trivial type.
- `byteCount`: The number of bytes to copy.   must not be   negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/copymemory(from:bytecount:))*