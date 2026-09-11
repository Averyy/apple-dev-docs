# stillImageLensStabilizationInfo

**Framework**: Core Media  
**Kind**: property

Indicates information about the lens stabilization applied to the current still image buffer.

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
static let stillImageLensStabilizationInfo: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMStillImageLensStabilization>
```

#### Discussion

Sample buffers that have been captured with a lens stabilization module may have this attachment. Which provides information about the stabilization status during the capture. This key will not be present in sample buffers coming from cameras without a lens stabilization module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/stillimagelensstabilizationinfo)*