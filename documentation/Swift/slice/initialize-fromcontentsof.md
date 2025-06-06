# initialize(fromContentsOf:)

**Framework**: Swift  
**Kind**: method

Initializes the buffer slice’s memory with with every element of the source.

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
func initialize<Element>(fromContentsOf source: some Collection) -> Slice<Base>.Index where Base == UnsafeMutableBufferPointer<Element>
```

#### Return Value

The index one past the last element of the buffer slice initialized by this function.

#### Discussion

Prior to calling the `initialize(fromContentsOf:)` method on a buffer slice, the memory it references must be uninitialized, or the `Element` type must be a trivial type. After the call, the memory referenced by the buffer slice up to, but not including, the returned index is initialized. The buffer slice must reference enough memory to accommodate `source.count` elements.

The returned index is the index of the next uninitialized element in the buffer slice, one past the index of the last element written. If `source` contains no elements, the returned index is equal to the buffer slice’s `startIndex`. If `source` contains as many elements as the buffer slice can hold, the returned index is equal to to the slice’s `endIndex`.

> **Note**: `self.count` >= `source.count`

`self.count` >= `source.count`

> **Note**: The memory regions referenced by `source` and this buffer slice must not overlap.

The memory regions referenced by `source` and this buffer slice must not overlap.

## Parameters

- `source`: A collection of elements to be used to   initialize the buffer slice’s storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/initialize(fromcontentsof:))*