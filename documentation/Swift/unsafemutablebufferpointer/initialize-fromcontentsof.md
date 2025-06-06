# initialize(fromContentsOf:)

**Framework**: Swift  
**Kind**: method

Initializes the buffer’s memory with every element of the source.

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
func initialize(fromContentsOf source: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index
```

#### Return Value

The index one past the last element of the buffer initialized by this function.

#### Discussion

Prior to calling the `initialize(fromContentsOf:)` method on a buffer, the memory referenced by the buffer must be uninitialized, or the `Element` type must be a trivial type. After the call, the memory referenced by the buffer up to, but not including, the returned index is initialized. The buffer must reference enough memory to accommodate `source.count` elements.

The returned index is the position of the next uninitialized element in the buffer, one past the index of the last element written. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer can hold, the returned index is equal to the buffer’s `endIndex`.

> **Note**: `self.count` >= `source.count`

`self.count` >= `source.count`

> **Note**: The memory regions referenced by `source` and this buffer must not overlap.

The memory regions referenced by `source` and this buffer must not overlap.

## Parameters

- `source`: A collection of elements to be used to   initialize the buffer’s storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/initialize(fromcontentsof:))*