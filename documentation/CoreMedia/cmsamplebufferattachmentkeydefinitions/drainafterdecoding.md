# drainAfterDecoding

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample buffer should be drained after decoding.

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
static let drainAfterDecoding: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

This attachment is used at run time to indicate that a sample precedes a break in decode sequence and that it is appropriate to drain the decoder after decoding this sample. This attachment is not written to media files. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/drainafterdecoding)*