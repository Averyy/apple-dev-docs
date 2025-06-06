# hdr10(minLuminance:maxLuminance:opticalOutputScale:)

**Framework**: Core Animation  
**Kind**: method

Creates EDR metadata for HDR10 content based on the luminance characteristics of a mastering display.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func hdr10(minLuminance minNits: Float, maxLuminance maxNits: Float, opticalOutputScale scale: Float) -> CAEDRMetadata
```

#### Return Value

A new EDR metadata object.

#### Discussion

Any content greater than the maximum luminance (`maxNits`) may be clamped when displayed.

The values in the drawable’s texture are assumed to be proportional to the optical output (in cd/m^2) of the reference display. For example, if the optical output scale is 100, then a value of 1.0 is assumed to be 100 nits.

If the content is in a normalized pixel format, set `opticalOutputScale` to 10000.

## Parameters

- `minNits`: The minimum nits (cd/m^2) of the mastering display.
- `maxNits`: The maximum nits (cd/m^2) of the mastering display.
- `scale`: A scale factor relating (display-referred linear) extended range buffer values to the optical output of a reference display.

## See Also

- [class func hdr10(displayInfo: Data?, contentInfo: Data?, opticalOutputScale: Float) -> CAEDRMetadata](caedrmetadata/hdr10(displayinfo:contentinfo:opticaloutputscale:).md)
  Creates EDR metadata for HDR10 content based on mastering display color information and content light levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caedrmetadata/hdr10(minluminance:maxluminance:opticaloutputscale:))*