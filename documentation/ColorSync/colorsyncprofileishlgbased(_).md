# ColorSyncProfileIsHLGBased(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Returns a Boolean value indicating whether the profile uses ITU BT.2100 HLG transfer functions.

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
func ColorSyncProfileIsHLGBased(_: ColorSyncProfile!) -> Bool
```

```c
extern bool ColorSyncProfileIsHLGBased(ColorSyncProfileRef );
```

## See Also

### Inspecting color characteristics
- [func ColorSyncProfileIsWideGamut(ColorSyncProfile!) -> Bool](./colorsyncprofileiswidegamut%28_%29.md)
  Returns a Boolean value indicating whether the display profile describes a wide-gamut color space.
- [func ColorSyncProfileIsPQBased(ColorSyncProfile!) -> Bool](./colorsyncprofileispqbased%28_%29.md)
  Returns a Boolean value indicating whether the profile uses ITU BT.2100 PQ transfer functions.
- [func ColorSyncProfileIsMatrixBased(ColorSyncProfile!) -> Bool](./colorsyncprofileismatrixbased%28_%29.md)
  Returns a Boolean value indicating whether the profile is matrix-based.
- [func ColorSyncProfileEstimateGamma(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](./colorsyncprofileestimategamma%28_,_%29.md)
  Estimates the gamma of a profile.
- [func ColorSyncProfileVerify(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./colorsyncprofileverify%28_,_,_%29.md)
  Verifies whether a profile can be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileishlgbased(_:))*