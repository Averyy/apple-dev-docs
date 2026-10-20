# ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_:_:_:_:_:_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafeMutablePointer<Float>!, _ redMax: UnsafeMutablePointer<Float>!, _ redGamma: UnsafeMutablePointer<Float>!, _ greenMin: UnsafeMutablePointer<Float>!, _ greenMax: UnsafeMutablePointer<Float>!, _ greenGamma: UnsafeMutablePointer<Float>!, _ blueMin: UnsafeMutablePointer<Float>!, _ blueMax: UnsafeMutablePointer<Float>!, _ blueGamma: UnsafeMutablePointer<Float>!) -> Bool
```

```c
extern bool ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfileRef profile, float *redMin, float *redMax, float *redGamma, float *greenMin, float *greenMax, float *greenGamma, float *blueMin, float *blueMax, float *blueGamma);
```

#### Discussion

The function performs this conversion only if a `vcgt` tag exists in the profile and the conversion is possible.

## See Also

### Reading display gamma and profiles
- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithdisplayid%28_%29.md)
  Creates a profile for the specified display.
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](./colorsyncprofileestimategammawithdisplayid%28_,_%29.md)
  Estimates the gamma of the profile for the specified display.
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](./colorsyncprofilecreatedisplaytransfertablesfromvcgt%28_,_%29.md)
  Creates display transfer tables from the profile’s `vcgt` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:))*