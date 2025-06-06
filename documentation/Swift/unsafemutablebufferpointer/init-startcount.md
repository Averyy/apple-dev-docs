# init(start:count:)

**Framework**: Swift  
**Kind**: init

Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.

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
init(start: UnsafeMutablePointer<Element>?, count: Int)
```

## Parameters

- `start`: A pointer to the start of the buffer, or  . If   is   ,   must be zero. However,   may be zero even for a   non-   . The pointer passed as   must be aligned to   .
- `count`: The number of instances in the buffer.   must not be   negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/init(start:count:))*