# kColorSyncTransformFullConversionData

**Framework**: ColorSync  
**Kind**: var

A key for the full-conversion code fragment, containing all non-`NULL` components from the profile sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var kColorSyncTransformFullConversionData: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncTransformParametricConversionData: Unmanaged<CFString>!](kcolorsynctransformparametricconversiondata.md)
  A key for the parametric code fragment, consisting only of parametric curves, matrices, and BPC components.
- [var kColorSyncTransformSimplifiedConversionData: Unmanaged<CFString>!](kcolorsynctransformsimplifiedconversiondata.md)
  A key for the simplified code fragment, collapsing the full conversion into one multi-dimensional table.
- [var kColorSyncConversionBPC: Unmanaged<CFString>!](kcolorsyncconversionbpc.md)
  A key for a black point compensation component, represented as a `CFArray` of `Float32` `CFNumber`s.
- [var kColorSyncFixedPointRange: Unmanaged<CFString>!](kcolorsyncfixedpointrange.md)
  A key for the fixed-point range of the conversion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynctransformfullconversiondata)*