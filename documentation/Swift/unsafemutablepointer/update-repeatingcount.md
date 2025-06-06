# update(repeating:count:)

**Framework**: Swift  
**Kind**: method

Update this pointer’s initialized memory with the specified number of consecutive copies of the given value.

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
func update(repeating repeatedValue: Pointee, count: Int)
```

#### Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized or `Pointee` must be a trivial type. After calling `update(repeating:count:)`, the region is initialized.

## Parameters

- `repeatedValue`: The value used when updating this pointer’s memory.
- `count`: The number of consecutive elements to update.    must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/update(repeating:count:))*