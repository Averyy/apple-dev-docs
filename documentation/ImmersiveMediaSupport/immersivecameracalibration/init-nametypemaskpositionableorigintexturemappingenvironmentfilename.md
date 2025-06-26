# init(name:type:mask:positionable:origin:textureMapping:environmentFilename:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a mesh based calibration from USDZ data and a image-based mask.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(name: String, type: ImmersiveCameraCalibration.CalibrationType, mask: ImmersiveCameraMask? = nil, positionable: Bool = false, origin: ImmersiveCameraCalibration.CameraOrigin = .zero, textureMapping: ImmersiveCameraCalibration.CameraTextureMapping = .identity, environmentFilename: String? = nil)
```

## Parameters

- `name`: Name identifying the calibration.
- `type`: The calibration type providing data to be used as the camera calibration for each eye.
- `mask`: Optional override mask definition describing the mask to be used for this calibration. If no mask is provided, the one inside LensParameters will be used.
- `positionable`: Flag indicating that this calibration can be anchored in mixed reality 3D space rather than being centered on the user’s eye position.
- `origin`: Position information that represents the origin from which to render the calibration in 3D space relative to the user’s eye.
- `textureMapping`: Texture mapping describing how each section of the video frame should be mapped into the calibration.
- `environmentFilename`: Stores the usdz file name for calibrations with a backdrop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/init(name:type:mask:positionable:origin:texturemapping:environmentfilename:))*