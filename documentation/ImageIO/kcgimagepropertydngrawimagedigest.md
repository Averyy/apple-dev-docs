# kCGImagePropertyDNGRawImageDigest

**Framework**: Image I/O  
**Kind**: var

A modified MD5 digest of the raw image data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let kCGImagePropertyDNGRawImageDigest: CFString
```

## See Also

- [let kCGImagePropertyDNGOriginalRawFileName: CFString](kcgimagepropertydngoriginalrawfilename.md)
  The file name of the original raw file.
- [let kCGImagePropertyDNGOriginalRawFileData: CFString](kcgimagepropertydngoriginalrawfiledata.md)
  The compressed contents of the original raw file.
- [let kCGImagePropertyDNGNoiseReductionApplied: CFString](kcgimagepropertydngnoisereductionapplied.md)
  The amount of noise reduction applied to the raw data on a scale of 0.0 to 1.0.
- [let kCGImagePropertyDNGNewRawImageDigest: CFString](kcgimagepropertydngnewrawimagedigest.md)
  An MD5 digest of the raw image data.
- [let kCGImagePropertyDNGOriginalRawFileDigest: CFString](kcgimagepropertydngoriginalrawfiledigest.md)
  An MD5 digest of the data stored for the original raw file data.
- [let kCGImagePropertyDNGOriginalDefaultFinalSize: CFString](kcgimagepropertydngoriginaldefaultfinalsize.md)
  THe default final size of the larger original file that was the source of this proxy.
- [let kCGImagePropertyDNGOriginalBestQualityFinalSize: CFString](kcgimagepropertydngoriginalbestqualityfinalsize.md)
  The best-quality final size of the larger original file that was the source of this proxy.
- [let kCGImagePropertyDNGOriginalDefaultCropSize: CFString](kcgimagepropertydngoriginaldefaultcropsize.md)
  The default crop size of the larger original file that was the source of this proxy.
- [let kCGImagePropertyDNGRawToPreviewGain: CFString](kcgimagepropertydngrawtopreviewgain.md)
  The gain between the main raw IFD and the preview IFD that contains this tag.
- [let kCGImagePropertyDNGNoiseProfile: CFString](kcgimagepropertydngnoiseprofile.md)
  The amount of noise in the raw image.
- [let kCGImagePropertyDNGCFALayout: CFString](kcgimagepropertydngcfalayout.md)
  The spatial layout of the CFA.
- [let kCGImagePropertyDNGCFAPlaneColor: CFString](kcgimagepropertydngcfaplanecolor.md)
  A mapping between the values in the CFA pattern tag and the plane numbers in linear raw space.
- [let kCGImagePropertyDNGOpcodeList1: CFString](kcgimagepropertydngopcodelist1.md)
  The list of opcodes to apply to the raw image, as read directly from the file.
- [let kCGImagePropertyDNGOpcodeList2: CFString](kcgimagepropertydngopcodelist2.md)
  THe list of opcodes to apply to the raw image, after mapping it to linear reference values.
- [let kCGImagePropertyDNGOpcodeList3: CFString](kcgimagepropertydngopcodelist3.md)
  The list of opcodes to apply to the raw image, after demosaicing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertydngrawimagedigest)*