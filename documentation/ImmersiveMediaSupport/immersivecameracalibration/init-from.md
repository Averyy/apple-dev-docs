# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init(lensParameters: ImmersiveLensDefinition, mask: ImmersiveCameraMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(lensparameters:mask:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a parametric calibration from meiRives data and a image-based mask.
- [init(lensParameters: ImmersiveLensDefinition, maskDefinition: ImmersiveDynamicMask?, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(lensparameters:maskdefinition:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a parametric calibration from meiRives data and a dynamic mask.
- [init(usdzData: Data, mask: ImmersiveCameraMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(usdzdata:mask:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a image-based mask.
- [init(usdzData: Data, maskDefinition: ImmersiveDynamicMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(usdzdata:maskdefinition:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a dynamic mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/init(from:))*