# update(from:count:)

**Framework**: Swift  
**Kind**: method

Update this pointer’s initialized memory with the specified number of instances, copied from the given pointer’s memory.

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
func update(from source: UnsafePointer<Pointee>, count: Int)
```

#### Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized or `Pointee` must be a trivial type. After calling `update(from:count:)`, the region is initialized.

> **Note**: Returns without performing work if `self` and `source` are equal.

## Parameters

- `source`: A pointer to at least   initialized instances of type   . The memory regions referenced by   and this   pointer may overlap.
- `count`: The number of instances to copy from the memory referenced by    to this pointer’s memory.   must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/update(from:count:))*