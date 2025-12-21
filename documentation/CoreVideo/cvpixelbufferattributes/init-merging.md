# init(merging:)

**Framework**: Core Video  
**Kind**: init

Resolve multiple attribute specifications into a single instance.

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
init?(merging values: [CVPixelBufferAttributes])
```

#### Discussion

This is useful when you need to resolve multiple requirements between different potential clients of a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferattributes/init(merging:))*