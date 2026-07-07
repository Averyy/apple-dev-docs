# ExternalNonInteractiveAccessory

**Framework**: SwiftUI  
**Kind**: struct

A scene accessory that presents non-interactive content on an external display.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
struct ExternalNonInteractiveAccessory<Content> where Content : View
```

#### Overview

The scene accessory may be presented when an external display is connected to the device, or when the device is connected to an external display via AirPlay.

For example, you can define a scene accessory for previewing a non-interactive presentation, which may be presented when an external display is connected:

```swift
struct RootView: View {
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .sceneAccessory {
                ExternalNonInteractiveAccessory {
                    PresentationPreview(document: document)
                }
            }
    }
}
```

## Topics

### Initializers
- [init(content: () -> Content)](externalnoninteractiveaccessory/init(content:).md)
  Creates a scene accessory that presents non-interactive content on an external display.
- [init(isEnabled: Binding<Bool>, content: () -> Content)](externalnoninteractiveaccessory/init(isenabled:content:).md)
  Creates a scene accessory that presents non-interactive content on an external display with a binding for programmatic enablement.

## Relationships

### Conforms To
- [SceneAccessoryContent](sceneaccessorycontent.md)

## See Also

- [func sceneAccessory<C>(content: () -> C) -> some View](view/sceneaccessory(content:).md)
  Defines any scene accessories associated with `self`.
- [protocol SceneAccessoryContent](sceneaccessorycontent.md)
  Conforming types represent items which define content for scene accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/externalnoninteractiveaccessory)*