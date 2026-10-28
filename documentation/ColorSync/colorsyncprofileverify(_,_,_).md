# ColorSyncProfileVerify(_:_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Verifies whether a profile can be used.

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
func ColorSyncProfileVerify(_ prof: ColorSyncProfile!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?, _ warnings: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

```c
extern bool ColorSyncProfileVerify(ColorSyncProfileRef prof, CFErrorRef*errors, CFErrorRef*warnings);
```

## Return Value

`true` if the profile can be used; otherwise, `false`.

## Parameters

- `prof`: The profile to verify.
- `errors`: Returns error strings in case problems are found that would prevent use of the profile.
- `warnings`: Returns warning strings indicating problems due to lack of conformance with the ICC specification, but not preventing use of the profile.

## See Also

### Inspecting color characteristics
- [func ColorSyncProfileIsWideGamut(ColorSyncProfile!) -> Bool](./colorsyncprofileiswidegamut%28_%29.md)
  Returns a Boolean value indicating whether the display profile describes a wide-gamut color space.
- [func ColorSyncProfileIsPQBased(ColorSyncProfile!) -> Bool](./colorsyncprofileispqbased%28_%29.md)
  Returns a Boolean value indicating whether the profile uses ITU BT.2100 PQ transfer functions.
- [func ColorSyncProfileIsHLGBased(ColorSyncProfile!) -> Bool](./colorsyncprofileishlgbased%28_%29.md)
  Returns a Boolean value indicating whether the profile uses ITU BT.2100 HLG transfer functions.
- [func ColorSyncProfileIsMatrixBased(ColorSyncProfile!) -> Bool](./colorsyncprofileismatrixbased%28_%29.md)
  Returns a Boolean value indicating whether the profile is matrix-based.
- [func ColorSyncProfileEstimateGamma(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](./colorsyncprofileestimategamma%28_,_%29.md)
  Estimates the gamma of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileverify(_:_:_:))*