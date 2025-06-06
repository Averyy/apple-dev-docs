# kCMSampleAttachmentKey_PartialSync

**Framework**: Core Media  
**Kind**: var

Indicates whether the sample is a partial sync sample (type `CFBoolean`, default false).

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
let kCMSampleAttachmentKey_PartialSync: CFString
```

#### Discussion

A partial sync sample can be decoded without requiring any previous samples to have been decoded. Samples following two consecutive partial sync samples also do not require samples prior to the pair to have been decoded. To treat a sample as a partial sync sample, set a value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for both this key and the [`kCMSampleAttachmentKey_NotSync`](kcmsampleattachmentkey_notsync.md) key.

This attachment is read from and written to media files.

## See Also

- [let kCMSampleAttachmentKey_NotSync: CFString](kcmsampleattachmentkey_notsync.md)
  Indicates whether the sample is a sync sample (type `CFBoolean`, default false).
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
- [let kCMSampleAttachmentKey_PostDecodeProcessingMetadata: CFString](kcmsampleattachmentkey_postdecodeprocessingmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_partialsync)*