# init(name:type:mask:positionable:origin:textureMapping:environmentFilename:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a mesh based calibration from USDZ data and a image-based mask.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(name: String, type: ImmersiveCameraCalibration.CalibrationType, mask: ImmersiveCameraMask? = nil, positionable: Bool = false, origin: ImmersiveCameraCalibration.CameraOrigin = .zero, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping = .identity, environmentFilename: String? = nil)
```

## Parameters

- `name`: The name to identify the calibration.
- `type`: The calibration type providing data to be used as the camera calibration for each eye.
- `mask`: Optional override mask definition describing the mask to be used for this calibration. If no mask is provided, the one inside LensParameters will be used.
- `positionable`: A flag that indicates whether to anchor this calibration in mixed reality 3D space rather than centering it on the person’s eye position.
- `origin`: The position information that represents the origin from which to render the calibration in 3D space relative to the person’s eye.
- `textureMapping`: The texture mapping that describes how each section of the video frame maps into the calibration.
- `environmentFilename`: The USDZ filename for calibrations with a backdrop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/init(name:type:mask:positionable:origin:texturemapping:environmentfilename:))*