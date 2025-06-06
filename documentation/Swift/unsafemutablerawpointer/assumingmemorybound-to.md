# assumingMemoryBound(to:)

**Framework**: Swift  
**Kind**: method

Returns a typed pointer to the memory referenced by this pointer, assuming that the memory is already bound to the specified type.

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
func assumingMemoryBound<T>(to: T.Type) -> UnsafeMutablePointer<T> where T : ~Copyable
```

#### Return Value

A typed pointer to the same memory as this raw pointer.

#### Discussion

Use this method when you have a raw pointer to memory that has  been bound to the specified type. The memory starting at this pointer must be bound to the type `T`. Accessing memory through the returned pointer is undefined if the memory has not been bound to `T`. To bind memory to `T`, use `bindMemory(to:capacity:)` instead of this method.

## Parameters

- `to`: The type   that the memory has already been bound to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/assumingmemorybound(to:))*