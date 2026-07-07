# sceneAccessory(content:)

**Framework**: SwiftUI  
**Kind**: method

Defines any scene accessories associated with `self`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func sceneAccessory<C>(@ContentBuilder content: () -> C) -> some View where C : SceneAccessoryContent
```

#### Discussion

A scene accessory declares supplementary content that the system presents on the app’s behalf when an associated piece of system functionality becomes available, for example when an external display is connected. The app declares what content to provide; the system decides when and where to present it. Scene accessories enhance the app’s experience when available, but the app must remain fully functional without them.

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

Use the `SceneAccessoryContent/onAvailabilityChange` modifier to observe a scene accessory’s system-determined availability. Observe the lifecycle of the accessory’s content using `View/onAppear`, `View/onDisappear`, and [`scenePhase`](environmentvalues/scenephase.md).

For example, you can present various controls based on the scene accessory’s current state:

```swift
struct RootView: View {
    @State private var isEnabled = false
    @State private var isAvailable = false
    @State private var isPresented = false
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .toolbar {
                if isAvailable {
                    // Include a toolbar button to enable the
                    // scene accessory when a display is available.
                    SecondaryDisplayToggle(isEnabled: $isEnabled)

                    // Include additional toolbar controls once the
                    // accessory is presented.
                    if isPresented {
                        SecondaryDisplayControls()
                    }
                }
            }
            .sceneAccessory {
                ExternalNonInteractiveAccessory(
                    isEnabled: $isEnabled
                ) {
                    PresentationPreview(document: document)
                        .onAppear { isPresented = true }
                        .onDisappear { isPresented = false }
                }
                .onAvailabilityChange { newValue in
                    isAvailable = newValue
                }
            }
    }
}
```

## See Also

- [protocol SceneAccessoryContent](sceneaccessorycontent.md)
  Conforming types represent items which define content for scene accessories.
- [struct ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md)
  A scene accessory that presents non-interactive content on an external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sceneaccessory(content:))*