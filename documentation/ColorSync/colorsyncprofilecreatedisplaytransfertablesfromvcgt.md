# ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_:_:)

**Framework**: ColorSync  
**Kind**: func

Creates display transfer tables from the profile’s `vcgt` tag.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_ profile: ColorSyncProfile!, _ nSamplesPerChannel: UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?
```

#### Discussion

Creates three tables of floats (a red table, a green table, and a blue table), each of size `nSamplesPerChannel`, packed into contiguous memory contained in the returned `CFDataRef`, from the `vcgt` tag of the profile (if a `vcgt` tag exists in the profile). `CGSetDisplayTransferByTable` uses these tables.

## See Also

- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithdisplayid(_:).md)
  Creates a profile for the specified display.
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategammawithdisplayid(_:_:).md)
  Estimates the gamma of the profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:).md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:))*