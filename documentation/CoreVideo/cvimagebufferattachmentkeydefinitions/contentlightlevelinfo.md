# contentLightLevelInfo

**Framework**: Core Video  
**Kind**: property

The content light level information for the image.

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
static var contentLightLevelInfo: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data> { get }
```

#### Discussion

The value for this key is a 4 byte big-endian data sequence to match the payload of the content light level information metadata in the supplemental enhancement information (SEI) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/contentlightlevelinfo)*