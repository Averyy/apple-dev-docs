# ColorSyncProfileEstimateGammaWithDisplayID(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Estimates the gamma of the profile for the specified display.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileEstimateGammaWithDisplayID(_ displayID: Int32, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float
```

```c
extern float ColorSyncProfileEstimateGammaWithDisplayID(const int32_t displayID, CFErrorRef*error);
```

## Return Value

A non-zero value on success, or `0.0` in case of error.

## Parameters

- `displayID`: The system-wide unique display ID (defined by IOKit).
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

### Reading display gamma and profiles
- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithdisplayid%28_%29.md)
  Creates a profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](./colorsyncprofilegetdisplaytransferformulafromvcgt%28_,_,_,_,_,_,_,_,_,_%29.md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](./colorsyncprofilecreatedisplaytransfertablesfromvcgt%28_,_%29.md)
  Creates display transfer tables from the profile’s `vcgt` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileestimategammawithdisplayid(_:_:))*