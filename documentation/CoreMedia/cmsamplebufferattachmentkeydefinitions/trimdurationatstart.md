# trimDurationAtStart

**Framework**: Core Media  
**Kind**: property

The duration that should be removed at the beginning of the sample buffer, after decoding.

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
static let trimDurationAtStart: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMTime>
```

#### Discussion

The getter returns the default value of [`zero`](cmtime/zero.md) (nothing removed) if this attachment is not present. In cases where all the output after decoding the sample buffer is to be discarded (for example, the samples are only being decoded to prime the decoder) the usual convention is to set [`trimDurationAtStart`](cmsamplebufferattachmentkeydefinitions/trimdurationatstart.md) to the whole duration and not to set a [`trimDurationAtEnd`](cmsamplebufferattachmentkeydefinitions/trimdurationatend.md) attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/trimdurationatstart)*