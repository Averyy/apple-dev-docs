# moveInitialize(from:count:)

**Framework**: Swift  
**Kind**: method

Moves instances from initialized source memory into the uninitialized memory referenced by this pointer, leaving the source memory uninitialized and the memory referenced by this pointer initialized.

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
func moveInitialize(from source: UnsafeMutablePointer<Pointee>, count: Int)
```

#### Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be uninitialized or `Pointee` must be a trivial type. After calling `moveInitialize(from:count:)`, the region is initialized and the memory region `source..<(source + count)` is uninitialized.

> **Note**: Returns without performing work if `self` and `source` are equal.

Returns without performing work if `self` and `source` are equal.

## Parameters

- `source`: A pointer to the values to copy. The memory region    must be initialized. The memory regions   referenced by   and this pointer may overlap.
- `count`: The number of instances to move from   to this   pointer’s memory.   must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/moveinitialize(from:count:))*