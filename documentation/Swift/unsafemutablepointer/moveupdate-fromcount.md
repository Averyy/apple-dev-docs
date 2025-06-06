# moveUpdate(from:count:)

**Framework**: Swift  
**Kind**: method

Update this pointer’s initialized memory by moving the specified number of instances the source pointer’s memory, leaving the source memory uninitialized.

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
func moveUpdate(from source: UnsafeMutablePointer<Pointee>, count: Int)
```

#### Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized or `Pointee` must be a trivial type. After calling `moveUpdate(from:count:)`, the region is initialized and the memory region `source..<(source + count)` is uninitialized.

> **Note**: The source and destination memory regions must not overlap.

The source and destination memory regions must not overlap.

## Parameters

- `source`: A pointer to the values to be moved. The memory region    must be initialized. The memory regions   referenced by   and this pointer must not overlap.
- `count`: The number of instances to move from   to this   pointer’s memory.   must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/moveupdate(from:count:))*