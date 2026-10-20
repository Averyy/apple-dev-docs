# hdr10(displayInfo:contentInfo:opticalOutputScale:)

**Framework**: Core Animation  
**Kind**: method

Creates EDR metadata for HDR10 content based on mastering display color information and content light levels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func hdr10(displayInfo displayData: Data?, contentInfo contentData: Data?, opticalOutputScale scale: Float) -> CAEDRMetadata
```

#### Discussion

The MDCV and CLLI message formats are defined in ISO/IEC 23008-2:2017.

The values in the drawable’s texture are assumed to be proportional to the optical output (in cd/m^2) of the reference display. For example, if the optical output scale is 100, then a value of 1.0 is assumed to be 100 nits.

## Parameters

- `displayData`: A value of 24 bytes that contains a big-endian structure, as defined in D.2.28 (Mastering Display Colour Volume SEI message).
- `contentData`: A value of 4 bytes that contains a big-endian structure, as defined in D.2.35 (Content Light Level Information SEI message).
- `scale`: A scale factor relating (display-referred linear) EDR values to the optical output of the reference display.

## See Also

- [class func hdr10(minLuminance: Float, maxLuminance: Float, opticalOutputScale: Float) -> CAEDRMetadata](caedrmetadata/hdr10(minluminance:maxluminance:opticaloutputscale:).md)
  Creates EDR metadata for HDR10 content based on the luminance characteristics of a mastering display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caedrmetadata/hdr10(displayinfo:contentinfo:opticaloutputscale:))*