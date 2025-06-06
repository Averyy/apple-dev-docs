# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a raw buffer over the contiguous bytes in the given typed buffer.

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
init<T>(_ buffer: UnsafeMutableBufferPointer<T>) where T : ~Copyable
```

## Parameters

- `buffer`: The typed buffer to convert to a raw buffer. The   buffer’s type   must be a trivial type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/init(_:)-rrzw)*