# contentLightLevelInfo

**Framework**: Core Video  
**Kind**: property

The content light level information for the image.

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
static var contentLightLevelInfo: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data> { get }
```

#### Discussion

The value for this key is a 4 byte big-endian data sequence to match the payload of the content light level information metadata in the supplemental enhancement information (SEI) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/contentlightlevelinfo)*