# deinitialize(count:)

**Framework**: Swift  
**Kind**: method

Deinitializes the specified number of values starting at this pointer.

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
func deinitialize(count: Int) -> UnsafeMutableRawPointer
```

#### Return Value

A raw pointer to the same address as this pointer. The memory referenced by the returned raw pointer is still bound to `Pointee`.

#### Discussion

The region of memory starting at this pointer and covering `count` instances of the pointer’s `Pointee` type must be initialized. After calling `deinitialize(count:)`, the memory is uninitialized, but still bound to the `Pointee` type.

## Parameters

- `count`: The number of instances to deinitialize.   must   not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/deinitialize(count:))*