# baseAddress

**Framework**: Swift  
**Kind**: property

A pointer to the first byte of the buffer.

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
var baseAddress: UnsafeRawPointer? { get }
```

#### Discussion

If the `baseAddress` of this buffer is `nil`, the count is zero. However, a buffer can have a `count` of zero even with a non-`nil` base address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/baseaddress)*