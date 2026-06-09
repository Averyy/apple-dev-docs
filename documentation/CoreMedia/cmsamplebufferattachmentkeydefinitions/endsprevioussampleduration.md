# endsPreviousSampleDuration

**Framework**: Core Media  
**Kind**: property

Indicates that sample buffer’s decode timestamp may be used to define the previous sample buffer’s duration.

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
static let endsPreviousSampleDuration: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

Marker sample buffers with this attachment may be used in situations where sample buffers are transmitted before their duration is known. In such situations, normally the recipient may use each sample buffer’s timestamp to calculate the duration of the previous sample buffer. The marker sample buffer with this attachment is sent to provide the timestamp for calculating the final sample buffer’s duration. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/endsprevioussampleduration)*