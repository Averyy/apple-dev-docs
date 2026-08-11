# ColorSyncProfileCreateWithDisplayID(_:)

**Framework**: ColorSync  
**Kind**: func

Creates a profile for the specified display.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileCreateWithDisplayID(_ displayID: UInt32) -> Unmanaged<ColorSyncProfile>?
```

#### Return Value

A new profile, or `NULL` in case of failure.

## Parameters

- `displayID`: The system-wide unique display ID (defined by IOKit); pass `0` for the main display.

## See Also

- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategammawithdisplayid(_:_:).md)
  Estimates the gamma of the profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:).md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:).md)
  Creates display transfer tables from the profile’s `vcgt` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatewithdisplayid(_:))*