# ColorSyncProfileCreateWithDisplayID(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Creates a profile for the specified display.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileCreateWithDisplayID(_ displayID: UInt32) -> Unmanaged<ColorSyncProfile>?
```

```c
extern ColorSyncProfileRefColorSyncProfileCreateWithDisplayID(uint32_t displayID);
```

#### Return Value

A new profile, or `NULL` in case of failure.

## Parameters

- `displayID`: The system-wide unique display ID (defined by IOKit); pass `0` for the main display.

## See Also

### Reading display gamma and profiles
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](./colorsyncprofileestimategammawithdisplayid%28_,_%29.md)
  Estimates the gamma of the profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](./colorsyncprofilegetdisplaytransferformulafromvcgt%28_,_,_,_,_,_,_,_,_,_%29.md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](./colorsyncprofilecreatedisplaytransfertablesfromvcgt%28_,_%29.md)
  Creates display transfer tables from the profile’s `vcgt` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatewithdisplayid(_:))*