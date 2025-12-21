# withUnsafeBuffer(_:)

**Framework**: Core Video  
**Kind**: method  
**Required**: Yes

Access the underlying `Buffer` object. This function should be used to bridge existing code that uses the Buffer type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withUnsafeBuffer<R>(_ body: (Self.Buffer) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferrepresentable/withunsafebuffer(_:))*