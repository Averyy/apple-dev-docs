# ColorSyncProfileIsPQBased(_:)

**Framework**: ColorSync  
**Kind**: func

Returns a Boolean value indicating whether the profile uses ITU BT.2100 PQ transfer functions.

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
func ColorSyncProfileIsPQBased(_: ColorSyncProfile!) -> Bool
```

## See Also

- [func ColorSyncProfileIsWideGamut(ColorSyncProfile!) -> Bool](colorsyncprofileiswidegamut(_:).md)
  Returns a Boolean value indicating whether the display profile describes a wide-gamut color space.
- [func ColorSyncProfileIsHLGBased(ColorSyncProfile!) -> Bool](colorsyncprofileishlgbased(_:).md)
  Returns a Boolean value indicating whether the profile uses ITU BT.2100 HLG transfer functions.
- [func ColorSyncProfileIsMatrixBased(ColorSyncProfile!) -> Bool](colorsyncprofileismatrixbased(_:).md)
  Returns a Boolean value indicating whether the profile is matrix-based.
- [func ColorSyncProfileEstimateGamma(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategamma(_:_:).md)
  Estimates the gamma of a profile.
- [func ColorSyncProfileVerify(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileverify(_:_:_:).md)
  Verifies whether a profile can be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileispqbased(_:))*