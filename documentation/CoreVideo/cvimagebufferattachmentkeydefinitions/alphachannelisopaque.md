# alphaChannelIsOpaque

**Framework**: Core Video  
**Kind**: property

True if the alpha channel in the image data is fully opaque.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var alphaChannelIsOpaque: CVAttachmentKeyDefinition<Self.ShouldPropagate, Bool> { get }
```

#### Discussion

This key is not used if the pixel format type has no alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/alphachannelisopaque)*