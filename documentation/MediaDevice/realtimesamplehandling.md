# RealtimeSampleHandling

**Framework**: Media Device  
**Kind**: protocol

A protocol that extends a media device extension to support realtime sample delivery.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol RealtimeSampleHandling : MediaDeviceExtension
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Realtime Video Processing

Use `ScreenCaptureKit` to receive system video samples, then use `VideoToolbox` for video sample encoding.

1. Provide an implementation of [`startRealtimeSampleDelivery(session:)`](realtimesamplehandling/startrealtimesampledelivery(session:).md).
2. Set up ScreenCaptureKit for a media device extension:

```swift
let picker = SCContentSharingPicker.shared()
picker.addObserver(self)
picker.active = true
```

1. Receive an `SCContentFilter` from the `SCContentSharingPicker` observer.
2. Create an `SCStream`. Call `addStreamOutput(_:type:sampleHandlerQueue:)`, and start with `startCapture()`.
3. Receive and process real time screen samples via the `SCStreamOutput` protocol.

#### Realtime Audio Processing

Use `AudioServerDriver` to receive system audio samples, then use `AudioToolbox` for audio sample encoding.

## Topics

### Instance Methods
- [func startRealtimeSampleDelivery(session: MediaOutputSession)](realtimesamplehandling/startrealtimesampledelivery(session:).md)
  Called when the extension can receive realtime samples.
- [func stopRealtimeSampleDelivery(session: MediaOutputSession)](realtimesamplehandling/stoprealtimesampledelivery(session:).md)
  Called when the extension should stop realtime sample delivery.

## Relationships

### Inherits From
- [AppExtension](../extensionfoundation/appextension.md)
- [MediaDeviceExtension](mediadeviceextension.md)

## See Also

- [class MediaOutputSession](mediaoutputsession.md)
  Represents a media output session for playing content on a remote device.
- [class MediaDeviceRoutingManager](mediadeviceroutingmanager.md)
  An object used by a [`MediaDeviceExtension`](mediadeviceextension.md) to report device discovery, state changes, and playback events back to the system.
- [struct MediaDeviceError](mediadeviceerror.md)
  An error returned by MediaDeviceExtension operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/realtimesamplehandling)*