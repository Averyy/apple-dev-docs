# trimDurationAtEnd

**Framework**: Core Media  
**Kind**: property

The duration that should be removed at the end of the sample buffer, after decoding.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let trimDurationAtEnd: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMTime>
```

#### Discussion

The getter returns the default value of [`zero`](cmtime/zero.md) (nothing removed) if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/trimdurationatend)*