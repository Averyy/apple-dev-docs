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
final func track(_ data: [DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation, image: CVPixelBuffer) async throws
```

#### Discussion

The device receives tracking vectors based on manually constructed observations.

Disable system tracking, then supply the observations at a fixed rate between 10 and 30 times per second. Any other rate is unsupported. Calling this method without first disabling system tracking is a fatal error.

> **Note**: [`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

## Parameters

- `data`: An array of   objects indicating the location of objects of interest in the frame.
- `cameraInformation`: The camera currently being used, and the orientation of the device.
- `image`: The captured camera image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/track(_:camerainformation:image:)-3uuza)*