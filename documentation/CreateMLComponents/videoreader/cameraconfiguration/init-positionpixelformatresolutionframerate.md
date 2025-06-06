# init(position:pixelFormat:resolution:frameRate:)

**Framework**: Create ML Components  
**Kind**: init

Creates a camera configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(position: VideoReader.CameraConfiguration.Position = .front, pixelFormat: VideoReader.CameraConfiguration.PixelFormat = .bgra32, resolution: VideoReader.CameraConfiguration.Resolution = .high, frameRate: Double = 30.0)
```

## Parameters

- `position`: The position of the camera. The default value is  . For devices with just one camera this value is ignored.
- `pixelFormat`: The pixel format of the camera frames. The default is  .
- `resolution`: The camera resolution. The default values is  .
- `frameRate`: The camera frame rate. The default value is 30.0 frames per second.

## See Also

- [init()](videoreader/cameraconfiguration/init.md)
  Creates a camera configuration.
- [VideoReader.CameraConfiguration.PixelFormat](videoreader/cameraconfiguration/pixelformat-swift.enum.md)
  The camera pixel format.
- [VideoReader.CameraConfiguration.Position](videoreader/cameraconfiguration/position-swift.enum.md)
  The position of the camera for an iOS device.
- [VideoReader.CameraConfiguration.Resolution](videoreader/cameraconfiguration/resolution-swift.enum.md)
  The camera resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraconfiguration/init(position:pixelformat:resolution:framerate:))*