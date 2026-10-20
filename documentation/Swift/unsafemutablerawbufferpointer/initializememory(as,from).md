# initializeMemory(as:from:)

**Framework**: Swift  
**Kind**: method

Initializes the buffer’s memory with the given elements, binding the initialized memory to the elements’ type.

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
func initializeMemory<S>(as type: S.Element.Type, from source: S) -> (unwritten: S.Iterator, initialized: UnsafeMutableBufferPointer<S.Element>) where S : Sequence
```

#### Return Value

An iterator to any elements of `source` that didn’t fit in the buffer, and a typed buffer of the written elements. The returned buffer references memory starting at the same base address as this buffer.

#### Discussion

When calling the `initializeMemory(as:from:)` method on a buffer `b`, the memory referenced by `b` must be uninitialized or initialized to a trivial type, and must be properly aligned for accessing `S.Element`. The buffer must contain sufficient memory to accommodate `source.underestimatedCount`.

This method initializes the buffer with elements from `source` until `source` is exhausted or, if `source` is a sequence but not a collection, the buffer has no more room for source’s elements. After calling `initializeMemory(as:from:)`, the memory referenced by the returned `UnsafeMutableBufferPointer` instance is bound and initialized to type `S.Element`. This method does not change the binding state of the unused portion of `b`, if any.

## Parameters

- `type`: The type of element to which this buffer’s memory will be bound.
- `source`: A sequence of elements with which to initialize the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/initializememory(as:from:))*