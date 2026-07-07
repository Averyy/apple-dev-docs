# resumeOutput

**Framework**: Core Media  
**Kind**: property

If present, indicates that output should be resumed following a discontinuity.

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
static let resumeOutput: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

This attachment is used at run time to request that a decode pipeline resume producing output after a discontinuity announced using the [`kCMSampleBufferConduitNotification_InhibitOutputUntil`](kcmsamplebufferconduitnotification_inhibitoutputuntil.md) notification. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/resumeoutput)*