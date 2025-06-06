# initialize(from:count:)

**Framework**: Swift  
**Kind**: method

Initializes the memory referenced by this pointer with the values starting at the given pointer.

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
func initialize(from source: UnsafePointer<Pointee>, count: Int)
```

#### Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be uninitialized or `Pointee` must be a trivial type. After calling `initialize(from:count:)`, the region is initialized.

> **Note**: The source and destination memory regions must not overlap.

The source and destination memory regions must not overlap.

## Parameters

- `source`: A pointer to the values to copy. The memory region    must be initialized. The memory regions   referenced by   and this pointer must not overlap.
- `count`: The number of instances to move from   to this   pointer’s memory.   must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(from:count:))*