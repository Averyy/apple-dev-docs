# onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)

**Framework**: SwiftUI  
**Kind**: method

Used to register an action triggered by system capture events.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func onCameraCaptureEvent(isEnabled: Bool = true, defaultSoundDisabled: Bool = false, action: @escaping (AVCaptureEvent) -> Void) -> some View
```

#### Discussion

Events may or may not be sent to applications based on the current system state. Backgrounded applications will not receive events, additionally events will only be sent to applications that are actively using the camera.

If an event from one source begins, then events from other sources will be ignored until the first event ends or is cancelled.

This API is for media capture use cases only.

## Parameters

- `isEnabled`: A boolean value indicating whether capture events trigger the provided action or not.   Set this value to   when your application cannot or will not respond to the action callbacks to avoid non-interactive buttons or UI elements.
- `defaultSoundDisabled`: A boolean value indicating whether or not the default sound is disabled.
- `action`: An event handler called when either the primary or secondary events are triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncameracaptureevent(isenabled:defaultsounddisabled:action:))*