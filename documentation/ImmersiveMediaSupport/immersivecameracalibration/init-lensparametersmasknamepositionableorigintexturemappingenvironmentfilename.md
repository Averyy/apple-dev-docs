# init(lensParameters:mask:name:positionable:origin:textureMapping:environmentFilename:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a parametric calibration from meiRives data and a image-based mask.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(lensParameters: ImmersiveLensDefinition, mask: ImmersiveCameraMask, name: String = "", positionable: Bool = false, origin: ImmersiveCameraCalibration.CameraOrigin = .zero, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping = .identity, environmentFilename: String? = nil)
```

## Parameters

- `lensParameters`: The   to be used as this camera calibration.
- `mask`: Override mask to be used for this calibration (instead of the mask contained in the lensParameters).
- `name`: Name identifying the calibration.
- `positionable`: Flag indicating that this calibration can be anchored in mixed reality 3D space rather than being centered on the user’s eye position.
- `origin`: Position information that represents the origin from which to render the calibration in 3D space relative to the user’s eye.
- `textureMapping`: Texture mapping describing how each section of the video frame should be mapped into the calibration.
- `environmentFilename`: Stores the usdz file name for calibrations with a backdrop.

## See Also

- [init(from: any Decoder) throws](immersivecameracalibration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(lensParameters: ImmersiveLensDefinition, maskDefinition: ImmersiveDynamicMask?, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(lensparameters:maskdefinition:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a parametric calibration from meiRives data and a dynamic mask.
- [init(usdzData: Data, mask: ImmersiveCameraMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(usdzdata:mask:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a image-based mask.
- [init(usdzData: Data, maskDefinition: ImmersiveDynamicMask, name: String, positionable: Bool, origin: ImmersiveCameraCalibration.CameraOrigin, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping, environmentFilename: String?)](immersivecameracalibration/init(usdzdata:maskdefinition:name:positionable:origin:texturemapping:environmentfilename:).md)
  Creates a mesh based calibration from USDZ data and a dynamic mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/init(lensparameters:mask:name:positionable:origin:texturemapping:environmentfilename:))*