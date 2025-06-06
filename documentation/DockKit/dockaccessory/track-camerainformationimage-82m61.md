# track(_:cameraInformation:image:)

**Framework**: DockKit  
**Kind**: method

Automatically generate and send tracking vectors to the device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 2.1+

## Declaration

```swift
final func track(_ metadata: [AVMetadataObject], cameraInformation: DockAccessory.CameraInformation, image: CVPixelBuffer) async throws
```

#### Discussion

The vectors are based on metadata coming from the camera.

Disable system tracking, then supply the observations at a fixed rate between 10 and 30 times per second. Any other rate is unsupported.

> **Note**: [`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

[`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

## Parameters

- `metadata`: An array of   objects indicating the location of objects within the frame.
- `cameraInformation`: The camera in current use and its orientation.
- `image`: The captured camera image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/track(_:camerainformation:image:)-82m61)*