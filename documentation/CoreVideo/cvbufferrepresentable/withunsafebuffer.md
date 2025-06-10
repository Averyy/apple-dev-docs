# withUnsafeBuffer(_:)

**Framework**: Core Video  
**Kind**: method  
**Required**: Yes

Access the underlying `Buffer` object. This function should be used to bridge existing code that uses the Buffer type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func withUnsafeBuffer<R>(_ body: (Self.Buffer) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferrepresentable/withunsafebuffer(_:))*