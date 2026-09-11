# emptyMedia

**Framework**: Core Media  
**Kind**: property

Marks an intentionally empty interval in the sequence of samples.

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
static let emptyMedia: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

The sample buffer’s output presentation timestamp indicates when the empty interval begins. Marker sample buffers with this attachment are used to announce the arrival of empty edits. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/emptymedia)*