# kCMSampleAttachmentKey_SMPTE_ST_2094_50Data

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
let kCMSampleAttachmentKey_SMPTE_ST_2094_50Data: CFString
```

```c
extern CFStringRef const kCMSampleAttachmentKey_SMPTE_ST_2094_50Data;
```

## Discussion

SMPTE ST 2094-50 per frame metadata

The attachment is CFData containing SMPTE ST 2094-50 metadata (SMPTE ST 2094-50:2026-08 — Dynamic Metadata for Color Volume Transform — Application #5). This attachment will override any SMPTE ST 2094-50 metadata stored within the compressed data. The data shall start with the field smpte_st_2094_50_application_info. Annex C, Section C.2.1 Table C.1


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_smpte_st_2094_50data)*