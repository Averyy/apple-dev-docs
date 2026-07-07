# displayEmptyMediaImmediately

**Framework**: Core Media  
**Kind**: property

Indicates that the empty marker should be dequeued immediately regardless of its timestamp.

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
static let displayEmptyMediaImmediately: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

Marker sample buffers with this attachment in addition to [`emptyMedia`](cmsamplebufferattachmentkeydefinitions/emptymedia.md) are used to tell that the empty sample buffer should be dequeued immediately regardless of its timestamp. This attachment should only be used with sample buffers with the [`emptyMedia`](cmsamplebufferattachmentkeydefinitions/emptymedia.md) attachment. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/displayemptymediaimmediately)*