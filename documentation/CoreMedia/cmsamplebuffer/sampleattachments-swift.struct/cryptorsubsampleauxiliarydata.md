# cryptorSubsampleAuxiliaryData

**Framework**: Core Media  
**Kind**: property

Describes the ranges of protected and unprotected data within a protected sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var cryptorSubsampleAuxiliaryData: Data? { get set }
```

#### Discussion

The value should contain one or more `BytesOfClearData/BytesOfProtectedData` pairs as appears in the ‘senc’ box (see ISO/IEC 23001-7 section 7.2.2). The `BytesOfClearData` and the `BytesOfProtectedData` fields are 32-bit integers. Both are native endian in the Data. This attachment is not present if the CMSampleBuffer contains unprotected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/cryptorsubsampleauxiliarydata)*