# ColorSyncProfileEstimateGammaWithDisplayID(_:_:)

**Framework**: ColorSync  
**Kind**: func

Estimates the gamma of the profile for the specified display.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileEstimateGammaWithDisplayID(_ displayID: Int32, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float
```

#### Return Value

A non-zero value on success, or `0.0` in case of error.

## Parameters

- `displayID`: The system-wide unique display ID (defined by IOKit).
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithdisplayid(_:).md)
  Creates a profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:).md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:).md)
  Creates display transfer tables from the profile’s `vcgt` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileestimategammawithdisplayid(_:_:))*