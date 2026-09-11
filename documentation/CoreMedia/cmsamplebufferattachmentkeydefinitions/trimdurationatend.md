# trimDurationAtEnd

**Framework**: Core Media  
**Kind**: property

The duration that should be removed at the end of the sample buffer, after decoding.

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
static let trimDurationAtEnd: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMTime>
```

#### Discussion

The getter returns the default value of [`zero`](cmtime/zero.md) (nothing removed) if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/trimdurationatend)*