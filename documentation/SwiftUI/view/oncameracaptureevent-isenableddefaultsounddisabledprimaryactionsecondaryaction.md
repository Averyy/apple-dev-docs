# onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)

**Framework**: SwiftUI  
**Kind**: method

Used to register actions triggered by system capture events.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, defaultSoundDisabled: Bool = false, primaryAction: @escaping (AVCaptureEvent) -> Void, secondaryAction: @escaping (AVCaptureEvent) -> Void) -> some View
```

#### Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

This API is for media capture use cases only.

## Parameters

- `isEnabled`: A boolean value indicating whether capture events trigger the provided actions or not. Set this value to `false` when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.
- `defaultSoundDisabled`: A boolean value indicating whether or not the default sound is disabled.
- `primaryAction`: An event handler called when a primary capture event is triggered.
- `secondaryAction`: An event handler called when a secondary capture event is triggered.

## See Also

- [func onCameraCaptureEvent(isEnabled: Bool, action: (AVCaptureEvent) -> Void) -> some View](view/oncameracaptureevent(isenabled:action:).md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](view/oncameracaptureevent(isenabled:defaultsounddisabled:action:).md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled: Bool, primaryAction: (AVCaptureEvent) -> Void, secondaryAction: (AVCaptureEvent) -> Void) -> some View](view/oncameracaptureevent(isenabled:primaryaction:secondaryaction:).md)
  Used to register actions triggered by system capture events.
- [func cameraAnchor(isActive: Bool) -> some View](view/cameraanchor(isactive:).md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:primaryaction:secondaryaction:))*