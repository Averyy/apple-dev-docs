# moveInitializeMemory(as:from:count:)

**Framework**: Swift  
**Kind**: method

Initializes the memory referenced by this pointer with the values starting at the given pointer, binds the memory to the values’ type, deinitializes the source memory, and returns a typed pointer to the newly initialized memory.

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
@discardableResult
func moveInitializeMemory<T>(as type: T.Type, from source: UnsafeMutablePointer<T>, count: Int) -> UnsafeMutablePointer<T> where T : ~Copyable
```

#### Return Value

A typed pointer to the memory referenced by this raw pointer.

#### Discussion

The memory referenced by this pointer must be uninitialized or initialized to a trivial type, and must be properly aligned for accessing `T`.

The memory in the region `source..<(source + count)` may overlap with the destination region. The `moveInitializeMemory(as:from:count:)` method automatically performs a forward or backward copy of all instances from the source region to their destination.

After calling this method on a raw pointer `p`, the region starting at `p` and continuing up to `p + count * MemoryLayout<T>.stride` is bound to type `T` and initialized. If `T` is a nontrivial type, you must eventually deinitialize or move from the values in this region to avoid leaks. Any memory in the region `source..<(source + count)` that does not overlap with the destination region is returned to an uninitialized state.

## Parameters

- `type`: The type to bind this memory to.
- `source`: A pointer to the values to copy. The memory in the region    must be initialized to type  .
- `count`: The number of copies of   to copy into memory.    must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/moveinitializememory(as:from:count:))*