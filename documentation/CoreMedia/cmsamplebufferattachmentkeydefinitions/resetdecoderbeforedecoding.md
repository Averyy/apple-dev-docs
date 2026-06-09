# resetDecoderBeforeDecoding

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample buffer should be reset before decoding.

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
static let resetDecoderBeforeDecoding: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

This attachment is used at run time to indicate that a sample follows a break in decode sequence and that it is appropriate to reset the decoder before decoding this sample. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/resetdecoderbeforedecoding)*