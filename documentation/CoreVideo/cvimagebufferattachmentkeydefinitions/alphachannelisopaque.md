# alphaChannelIsOpaque

**Framework**: Core Video  
**Kind**: property

True if the alpha channel in the image data is fully opaque.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var alphaChannelIsOpaque: CVAttachmentKeyDefinition<Self.ShouldPropagate, Bool> { get }
```

#### Discussion

This key is not used if the pixel format type has no alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/alphachannelisopaque)*