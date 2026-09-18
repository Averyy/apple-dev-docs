# CameraCaptureAccessory

**Framework**: SwiftUI  
**Kind**: struct

A scene accessory that presents content during camera capture.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
struct CameraCaptureAccessory<Content> where Content : View
```

#### Overview

The accessory may be presented while the app is in the foreground and has an active camera capture session. The system determines whether and where to present it. Unlike [`ExternalNonInteractiveAccessory`](externalnoninteractiveaccessory.md), the content can be interactive.

For example, you can present a teleprompter that the person being captured can read while looking toward the camera:

```swift
struct CameraRootView: View {
    @State private var model = TeleprompterModel()

    var body: some View {
        CameraView(model: model)
            .sceneAccessory {
                CameraCaptureAccessory {
                    TeleprompterView(model: model)
                }
            }
    }
}
```

## Topics

### Initializers
- [init(content: () -> Content)](cameracaptureaccessory/init(content:).md)
  Creates a scene accessory that presents content during camera capture.
- [init(isEnabled: Binding<Bool>, content: () -> Content)](cameracaptureaccessory/init(isenabled:content:).md)
  Creates a scene accessory that presents content during camera capture, with a binding for programmatic enablement.

## Relationships

### Conforms To
- [SceneAccessoryContent](sceneaccessorycontent.md)

## See Also

- [func sceneAccessory<C>(content: () -> C) -> some View](view/sceneaccessory(content:).md)
  Defines any scene accessories associated with `self`.
- [protocol SceneAccessoryContent](sceneaccessorycontent.md)
  Conforming types represent items which define content for scene accessories.
- [struct ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md)
  A scene accessory that presents non-interactive content on an external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/cameracaptureaccessory)*