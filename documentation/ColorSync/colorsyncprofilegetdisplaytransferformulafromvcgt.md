# ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_:_:_:_:_:_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafeMutablePointer<Float>!, _ redMax: UnsafeMutablePointer<Float>!, _ redGamma: UnsafeMutablePointer<Float>!, _ greenMin: UnsafeMutablePointer<Float>!, _ greenMax: UnsafeMutablePointer<Float>!, _ greenGamma: UnsafeMutablePointer<Float>!, _ blueMin: UnsafeMutablePointer<Float>!, _ blueMax: UnsafeMutablePointer<Float>!, _ blueGamma: UnsafeMutablePointer<Float>!) -> Bool
```

## See Also

- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithdisplayid(_:).md)
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategammawithdisplayid(_:_:).md)
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:))*