# onAvailabilityChange(perform:)

**Framework**: SwiftUI  
**Kind**: method

Defines a callback for observing the availability of `self`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func onAvailabilityChange(perform action: @escaping (Bool) -> Void) -> some SceneAccessoryContent
```

#### Discussion

When the availability of a scene accessory changes, the specified closure will be called.

For example, you can include additional controls based on the availability:

```swift
struct RootView: View {
    @State private var isEnabled = false
    @State private var isAvailable = false
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .toolbar {
                if isAvailable {
                    // Include a toolbar button to enable the
                    // scene accessory when a display is available.
                    SecondaryDisplayToggle(isEnabled: $isEnabled)
                }
            }
            .sceneAccessory {
                ExternalNonInteractiveAccessory(
                    isEnabled: $isEnabled
                ) {
                    PresentationPreview(document: document)
                }
                .onAvailabilityChange { newValue in
                    isAvailable = newValue
                }
            }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sceneaccessorycontent/onavailabilitychange(perform:))*