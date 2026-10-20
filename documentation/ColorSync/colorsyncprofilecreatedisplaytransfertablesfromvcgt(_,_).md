# ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Creates display transfer tables from the profile’s `vcgt` tag.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_ profile: ColorSyncProfile!, _ nSamplesPerChannel: UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?
```

```c
extern CFDataRefColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfileRef profile, size_t *nSamplesPerChannel);
```

#### Discussion

Creates three tables of floats (a red table, a green table, and a blue table), each of size `nSamplesPerChannel`, packed into contiguous memory contained in the returned `CFDataRef`, from the `vcgt` tag of the profile (if a `vcgt` tag exists in the profile). `CGSetDisplayTransferByTable` uses these tables.

## See Also

### Reading display gamma and profiles
- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithdisplayid%28_%29.md)
  Creates a profile for the specified display.
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](./colorsyncprofileestimategammawithdisplayid%28_,_%29.md)
  Estimates the gamma of the profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](./colorsyncprofilegetdisplaytransferformulafromvcgt%28_,_,_,_,_,_,_,_,_,_%29.md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:))*