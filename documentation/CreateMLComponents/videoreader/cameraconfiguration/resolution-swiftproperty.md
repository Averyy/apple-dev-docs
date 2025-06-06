# resolution

**Framework**: Create ML Components  
**Kind**: property

The camera resolution specifying the quality of the video output. The default values is `.high`

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var resolution: VideoReader.CameraConfiguration.Resolution
```

## See Also

- [var cameraPosition: VideoReader.CameraConfiguration.Position](videoreader/cameraconfiguration/cameraposition.md)
  The camera position. For an iOS device this can be either `.front` or `.rear`. For devices with just one camera this value is ignored. The default value is `.front`.
- [var frameRate: Double](videoreader/cameraconfiguration/framerate.md)
  The camera frame rate. The default value is 30.0 frames per second.
- [var pixelFormat: VideoReader.CameraConfiguration.PixelFormat](videoreader/cameraconfiguration/pixelformat-swift.property.md)
  The camera pixel format. The default is `.bgra32`.
- [var position: VideoReader.CameraConfiguration.Position](videoreader/cameraconfiguration/position-swift.property.md)
  The camera position. For an iOS device this can be either `.front` or `.rear`. For devices with just one camera this value is ignored. The default value is `.front`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraconfiguration/resolution-swift.property)*