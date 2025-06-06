# ColorSyncIterateInstalledProfilesWithOptions(_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncIterateInstalledProfilesWithOptions(_ callBack: ColorSyncProfileIterateCallback?, _ seed: UnsafeMutablePointer<UInt32>?, _ userInfo: UnsafeMutableRawPointer?, _ options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```

## See Also

- [func ColorSyncAPIVersion() -> UInt32](colorsyncapiversion().md)
- [func ColorSyncCreateCodeFragment(CFArray!, CFDictionary!) -> Unmanaged<CFTypeRef>!](colorsynccreatecodefragment(_:_:).md)
- [func ColorSyncProfileIsHLGBased(ColorSyncProfile!) -> Bool](colorsyncprofileishlgbased(_:).md)
- [func ColorSyncProfileIsMatrixBased(ColorSyncProfile!) -> Bool](colorsyncprofileismatrixbased(_:).md)
- [func ColorSyncProfileIsPQBased(ColorSyncProfile!) -> Bool](colorsyncprofileispqbased(_:).md)
- [func ColorSyncProfileIsWideGamut(ColorSyncProfile!) -> Bool](colorsyncprofileiswidegamut(_:).md)
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](colorsynctransformgetprofilesequence(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:))*