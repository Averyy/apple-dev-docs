# moveInitializeMemory(as:fromContentsOf:)

**Framework**: Swift  
**Kind**: method

Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this slice’s memory initialized.

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
func moveInitializeMemory<T>(as type: T.Type, fromContentsOf source: UnsafeMutableBufferPointer<T>) -> UnsafeMutableBufferPointer<T>
```

#### Return Value

A typed buffer referencing the initialized elements. The returned buffer references memory starting at the same base address as this slice, and its count is equal to `source.count`.

#### Discussion

When calling the `moveInitializeMemory(as:fromContentsOf:)` method, the memory referenced by the buffer slice must be uninitialized, or initialized to a trivial type. The buffer slice must reference enough memory to store `source.count` elements, and it must be properly aligned for accessing `C.Element`. After the method returns, the memory referenced by the returned buffer is initialized and the memory region underlying `source` is uninitialized.

This method initializes the buffer slice with the contents of `source` until `source` is exhausted. After calling `initializeMemory(as:fromContentsOf:)`, the memory referenced by the returned `UnsafeMutableBufferPointer` instance is bound to the type of `T` and is initialized. This method does not change the binding state of the unused portion of the buffer slice, if any.

## Parameters

- `type`: The type of element to which this buffer’s memory will be bound.
- `source`: A buffer referencing the values to copy.   The memory region underlying   must be initialized.   The memory regions referenced by   and this slice may overlap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/moveinitializememory(as:fromcontentsof:)-4gqrz)*