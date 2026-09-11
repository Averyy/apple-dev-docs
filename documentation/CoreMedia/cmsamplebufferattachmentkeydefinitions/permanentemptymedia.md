# permanentEmptyMedia

**Framework**: Core Media  
**Kind**: property

Marks the end of the sequence of samples.

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
static let permanentEmptyMedia: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

Marker sample buffers with this attachment in addition to [`emptyMedia`](cmsamplebufferattachmentkeydefinitions/emptymedia.md) are used to indicate that no further samples are expected. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/permanentemptymedia)*