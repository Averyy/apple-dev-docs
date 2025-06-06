# allocate(byteCount:alignment:)

**Framework**: Swift  
**Kind**: method

Allocates uninitialized memory with the specified size and alignment.

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
static func allocate(byteCount: Int, alignment: Int) -> UnsafeMutableRawPointer
```

#### Return Value

A pointer to a newly allocated region of memory. The memory is allocated, but not initialized.

#### Discussion

You are in charge of managing the allocated memory. Be sure to deallocate any memory that you manually allocate.

The allocated memory is not bound to any specific type and must be bound before performing any typed operations. If you are using the memory for a specific type, allocate memory using the `UnsafeMutablePointer.allocate(capacity:)` static method instead.

## Parameters

- `byteCount`: The number of bytes to allocate.   must not be   negative.
- `alignment`: The alignment of the new region of allocated memory, in   bytes.   must be a whole power of 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/allocate(bytecount:alignment:))*