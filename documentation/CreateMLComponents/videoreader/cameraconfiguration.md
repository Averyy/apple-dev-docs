# VideoReader.CameraConfiguration

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

The configuration of the camera to pass to the `readCamera` method.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct CameraConfiguration
```

## Topics

### Creating a camera configuration
- [init()](./cameraconfiguration/init%28%29.md)
  Creates a camera configuration.
- [init(position: VideoReader.CameraConfiguration.Position, pixelFormat: VideoReader.CameraConfiguration.PixelFormat, resolution: VideoReader.CameraConfiguration.Resolution, frameRate: Double)](./cameraconfiguration/init%28position,pixelformat,resolution,framerate%29.md)
  Creates a camera configuration.
- [VideoReader.CameraConfiguration.PixelFormat](./cameraconfiguration/pixelformat-swift.enum.md)
  The camera pixel format.
- [VideoReader.CameraConfiguration.Position](./cameraconfiguration/position-swift.enum.md)
  The position of the camera for an iOS device.
- [VideoReader.CameraConfiguration.Resolution](./cameraconfiguration/resolution-swift.enum.md)
  The camera resolution.
### Getting the properties
- [var cameraPosition: VideoReader.CameraConfiguration.Position](./cameraconfiguration/cameraposition.md)
  The camera position. For an iOS device this can be either `.front` or `.rear`. For devices with just one camera this value is ignored. The default value is `.front`.
- [var frameRate: Double](./cameraconfiguration/framerate.md)
  The camera frame rate. The default value is 30.0 frames per second.
- [var pixelFormat: VideoReader.CameraConfiguration.PixelFormat](./cameraconfiguration/pixelformat-swift.property.md)
  The camera pixel format. The default is `.bgra32`.
- [var position: VideoReader.CameraConfiguration.Position](./cameraconfiguration/position-swift.property.md)
  The camera position. For an iOS device this can be either `.front` or `.rear`. For devices with just one camera this value is ignored. The default value is `.front`.
- [var resolution: VideoReader.CameraConfiguration.Resolution](./cameraconfiguration/resolution-swift.property.md)
  The camera resolution specifying the quality of the video output. The default values is `.high`

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading
- [static read(_:)](./read%28_%29.md)
  Reads a sequence of annotated files as an array of annotated async sequences of video frames.
- [static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers](./readcamera%28configuration%29.md)
  Reads an async sequence of video frames captured with a video camera.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](./read%28contentsof%29.md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](./asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraAsyncBuffers](./cameraasyncbuffers.md)
  An async sequence of video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraconfiguration)*