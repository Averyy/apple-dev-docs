# ColorSyncProfileCopyHeadroomAdaptiveGainCurveMetadata

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Returns a copy of the raw Headroom Adaptive Gain Curve data embedded in a profile.

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
extern CFDataRefColorSyncProfileCopyHeadroomAdaptiveGainCurveMetadata(ColorSyncProfileRef profile);
```

## Mentions

- [Authoring Headroom Adaptive Gain Curve metadata](./authoring-headroom-adaptive-gain-curve-metadata.md)

## Return Value

A copy of the raw HAGC data that the caller must release with `CFRelease`, or `NULL` if the profile contains no HAGC tag.

## Parameters

- `profile`: The profile to read the HAGC tag from.

## See Also

### Reading a curve (C API)
- [ColorSyncProfileCopyHeadroomAdaptiveGainCurveInfoDictionary](./colorsyncprofilecopyheadroomadaptivegaincurveinfodictionary.md)
  Returns a dictionary describing the Headroom Adaptive Gain Curve decoded from a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopyheadroomadaptivegaincurvemetadata)*