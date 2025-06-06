# kCMSampleAttachmentKey_PostDecodeProcessingMetadata

**Framework**: Core Media  
**Kind**: var

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kCMSampleAttachmentKey_PostDecodeProcessingMetadata: CFString
```

## See Also

- [let kCMSampleAttachmentKey_NotSync: CFString](kcmsampleattachmentkey_notsync.md)
  Indicates whether the sample is a sync sample (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_PartialSync: CFString](kcmsampleattachmentkey_partialsync.md)
  Indicates whether the sample is a partial sync sample (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_DependsOnOthers: CFString](kcmsampleattachmentkey_dependsonothers.md)
  Indicates whether the sample depends on other samples for decoding (type `CFBoolean`).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_postdecodeprocessingmetadata)*