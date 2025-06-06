# kCMSampleAttachmentKey_DependsOnOthers

**Framework**: Core Media  
**Kind**: var

Indicates whether the sample depends on other samples for decoding (type `CFBoolean`).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMSampleAttachmentKey_DependsOnOthers: CFString
```

#### Discussion

This key has no default value. If this key is not present, dependency information for the sample is unknown. A value of [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) indicates that the sample does not depend on other samples (for example, an I frame).  A value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) indicates that the sample does depend on other samples (for example, a P or B frame).

This attachment is read from and written to media files.

## See Also

- [let kCMSampleAttachmentKey_NotSync: CFString](kcmsampleattachmentkey_notsync.md)
  Indicates whether the sample is a sync sample (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_PartialSync: CFString](kcmsampleattachmentkey_partialsync.md)
  Indicates whether the sample is a partial sync sample (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_IsDependedOnByOthers: CFString](kcmsampleattachmentkey_isdependedonbyothers.md)
  Indicates whether other samples depend on this sample for decoding (type `CFBoolean`).
- [let kCMSampleAttachmentKey_DisplayImmediately: CFString](kcmsampleattachmentkey_displayimmediately.md)
  Indicates whether the sample should be displayed immediately (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_DoNotDisplay: CFString](kcmsampleattachmentkey_donotdisplay.md)
  Indicates whether the sample should be decoded but not displayed (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_EarlierDisplayTimesAllowed: CFString](kcmsampleattachmentkey_earlierdisplaytimesallowed.md)
  Indicates whether later samples may have earlier display times (type `CFBoolean`).
- [let kCMSampleAttachmentKey_HasRedundantCoding: CFString](kcmsampleattachmentkey_hasredundantcoding.md)
  Indicates whether the sample has redundant coding (type `CFBoolean`).
- [let kCMSampleAttachmentKey_PostDecodeProcessingMetadata: CFString](kcmsampleattachmentkey_postdecodeprocessingmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_dependsonothers)*