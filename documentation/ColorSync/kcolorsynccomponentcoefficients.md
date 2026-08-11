# kColorSyncComponentCoefficients

**Framework**: ColorSync  
**Kind**: var

Sub-dictionary of custom linear-combination coefficients for free-style component mixing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var kColorSyncComponentCoefficients: Unmanaged<CFString>
```

#### Discussion

Each present key contributes its value as a weight in: `signal = R*red + G*green + B*blue + MAX*maxRGB + MIN*minRGB + C*component`. Only present when `kColorSyncComponentMix == 3`.

## See Also

- [var kColorSyncCoefficientBlue: Unmanaged<CFString>](kcolorsynccoefficientblue.md)
  Weight for the blue channel in the free-style component mixing sum.
- [var kColorSyncCoefficientComponent: Unmanaged<CFString>](kcolorsynccoefficientcomponent.md)
  Weight for the ‘component’ term in the free-style component mixing sum.
- [var kColorSyncCoefficientGreen: Unmanaged<CFString>](kcolorsynccoefficientgreen.md)
  Weight for the green channel in the free-style component mixing sum.
- [var kColorSyncCoefficientMaxRGB: Unmanaged<CFString>](kcolorsynccoefficientmaxrgb.md)
  Weight for the MAX(R,G,B) term in the free-style component mixing sum.
- [var kColorSyncCoefficientMinRGB: Unmanaged<CFString>](kcolorsynccoefficientminrgb.md)
  Weight for the MIN(R,G,B) term in the free-style component mixing sum.
- [var kColorSyncCoefficientRed: Unmanaged<CFString>](kcolorsynccoefficientred.md)
  Weight for the red channel in the free-style component mixing sum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynccomponentcoefficients)*