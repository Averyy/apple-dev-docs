# resetDecoderBeforeDecoding

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample buffer should be reset before decoding.

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
static let resetDecoderBeforeDecoding: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

This attachment is used at run time to indicate that a sample follows a break in decode sequence and that it is appropriate to reset the decoder before decoding this sample. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/resetdecoderbeforedecoding)*