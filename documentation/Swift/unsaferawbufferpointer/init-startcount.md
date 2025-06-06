# init(start:count:)

**Framework**: Swift  
**Kind**: init

Creates a buffer over the specified number of contiguous bytes starting at the given pointer.

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
init(start: UnsafeRawPointer?, count: Int)
```

## Parameters

- `start`: The address of the memory that starts the buffer. If    is  ,   must be zero. However,   may be zero even   for a non-   .
- `count`: The number of bytes to include in the buffer.   must not   be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/init(start:count:))*