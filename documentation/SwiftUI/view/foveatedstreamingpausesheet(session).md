# foveatedStreamingPauseSheet(session:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency func foveatedStreamingPauseSheet(session: Binding<FoveatedStreamingSession?>) -> some View
```

#### Discussion

Add this view modifier to inform the system that it should display UI for resuming the foveated streaming session when the person pauses the session. Otherwise, build your own UI that allows the person to resume the session by calling the `FoveatedStreamingSession/resume()` function.

## Parameters

- `session`: A binding to the foveated streaming session to display the pause sheet for. If `nil`, the system never displays the pause sheet.

## See Also

### Displaying media
- [struct CameraView](../../HomeKit/cameraview.md)
  A SwiftUI view into which a video stream or an image snapshot is rendered.
- [struct NowPlayingView](../../WatchKit/nowplayingview.md)
  A view that displays the system’s Now Playing interface so that the user can control audio.
- [struct VideoPlayer](../../AVKit/videoplayer.md)
  A view that displays content from a player and a native user interface to control playback.
- [func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect: ((AVContinuityDevice?) -> Void)?) -> some View](./continuitydevicepicker%28ispresented,ondidconnect%29.md)
  A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [func cameraAnchor(isActive: Bool) -> some View](./cameraanchor%28isactive%29.md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/foveatedstreamingpausesheet(session:))*