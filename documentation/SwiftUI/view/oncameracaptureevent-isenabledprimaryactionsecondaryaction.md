# onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)

**Framework**: SwiftUI  
**Kind**: method

Used to register actions triggered by system capture events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, primaryAction: @escaping (AVCaptureEvent) -> Void, secondaryAction: @escaping (AVCaptureEvent) -> Void) -> some View
```

#### Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

This API is for media capture use cases only.

## Parameters

- `isEnabled`: A boolean value indicating whether capture events trigger the provided actions or not.   Set this value to   when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.
- `primaryAction`: An event handler called when a primary capture event is triggered.
- `secondaryAction`: An event handler called when a secondary capture event is triggered.

## See Also

- [func onCameraCaptureEvent(isEnabled: Bool, action: (AVCaptureEvent) -> Void) -> some View](view/oncameracaptureevent(isenabled:action:).md)
  Used to register an action triggered by system capture events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:primaryaction:secondaryaction:))*