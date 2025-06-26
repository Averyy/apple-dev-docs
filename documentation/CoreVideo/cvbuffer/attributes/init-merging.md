# init(merging:)

**Framework**: Core Video  
**Kind**: init

Resolve multiple attribute specifications into a single instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated
- visionOS 26.0+ (Beta)

## Declaration

```swift
init?(merging values: [CVBuffer.Attributes])
```

#### Discussion

This is useful when you need to resolve multiple requirements between different potential clients of a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/attributes/init(merging:))*