# continuityDevicePicker(isPresented:onDidConnect:)

**Framework**: SwiftUI  
**Kind**: method

A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect: ((AVContinuityDevice?) -> Void)? = nil) -> some View
```

## Parameters

- `isPresented`: A   to whether the modal view is presented.
- `onDidConnect`: A closure executed when the picker successfully, connects AVContinuityDevice or nil if cancelled by a user.

## See Also

- [struct CameraView](../HomeKit/CameraView.md)
  A SwiftUI view into which a video stream or an image snapshot is rendered.
- [struct NowPlayingView](../WatchKit/NowPlayingView.md)
  A view that displays the system’s Now Playing interface so that the user can control audio.
- [struct VideoPlayer](../AVKit/VideoPlayer.md)
  A view that displays content from a player and a native user interface to control playback.
- [func cameraAnchor(isActive: Bool) -> some View](view/cameraanchor(isactive:).md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/continuitydevicepicker(ispresented:ondidconnect:))*