# cameraPosition

**Framework**: Create ML Components  
**Kind**: property  
**Role**: Instance Property

The camera position. For an iOS device this can be either `.front` or `.rear`. For devices with just one camera this value is ignored. The default value is `.front`.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0
- iPadOS 16.0+ - Deprecated in 17.0
- Mac Catalyst 16.0+ - Deprecated in 17.0
- macOS 13.0+ - Deprecated in 14.0
- visionOS 1.0+

> **Deprecated**: Use the position property instead.

## Declaration

```swift
var cameraPosition: VideoReader.CameraConfiguration.Position { get }
```

## See Also

### Getting the properties
- [var frameRate: Double](./framerate.md)
  The camera frame rate. The default value is 30.0 frames per second.
- [var pixelFormat: VideoReader.CameraConfiguration.PixelFormat](./pixelformat-swift.property.md)
  The camera pixel format. The default is `.bgra32`.
- [var position: VideoReader.CameraConfiguration.Position](./position-swift.property.md)
  The camera position. For an iOS device this can be either `.front` or `.rear`. For devices with just one camera this value is ignored. The default value is `.front`.
- [var resolution: VideoReader.CameraConfiguration.Resolution](./resolution-swift.property.md)
  The camera resolution specifying the quality of the video output. The default values is `.high`


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraconfiguration/cameraposition)*