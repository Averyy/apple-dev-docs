# ColorSyncProfileEstimateGamma(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Estimates the gamma of a profile.

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
func ColorSyncProfileEstimateGamma(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float
```

```c
extern float ColorSyncProfileEstimateGamma(ColorSyncProfileRef prof, CFErrorRef*error);
```

## Return Value

A non-zero value on success, or `0.0` in case of error.

## Parameters

- `prof`: The profile to perform estimation on.
- `error`: On failure, a pointer to an error describing the problem. Optional.

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
- [func ColorSyncProfileVerify(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./colorsyncprofileverify%28_,_,_%29.md)
  Verifies whether a profile can be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileestimategamma(_:_:))*