# ColorSyncProfileCopyHeadroomAdaptiveGainCurveInfoDictionary

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Returns a dictionary describing the Headroom Adaptive Gain Curve decoded from a profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```c
extern CFDictionaryRefColorSyncProfileCopyHeadroomAdaptiveGainCurveInfoDictionary(ColorSyncProfileRef profile);
```

#### Return Value

A dictionary describing the gain curve, which the caller must release with `CFRelease`, or `NULL` if the profile carries no HAGC tag. See the key constants declared below for the dictionary’s contents.

## Parameters

- `profile`: The profile to decode the HAGC tag from.

## See Also

### Reading a curve (C API)
- [ColorSyncProfileCopyHeadroomAdaptiveGainCurveMetadata](./colorsyncprofilecopyheadroomadaptivegaincurvemetadata.md)
  Returns a copy of the raw Headroom Adaptive Gain Curve data embedded in a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopyheadroomadaptivegaincurveinfodictionary)*