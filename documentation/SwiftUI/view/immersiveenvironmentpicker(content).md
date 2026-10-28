# immersiveEnvironmentPicker(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Add menu items to open immersive spaces from a media player’s environment picker.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func immersiveEnvironmentPicker<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View
```

## Discussion

These items are added alongside recently used system environments.

```swift
SystemPlayerView(player: player)
    .immersiveEnvironmentPicker {
        Button("Chalet", systemImage: "fireplace") {
            Task {
                await openImmersiveSpace(id: "Chalet")
            }
        }
    }
```

Use a [`UIViewControllerRepresentable`](../uiviewcontrollerrepresentable.md) instance to display a [`AVPlayerViewController`](../../AVKit/avplayerviewcontroller.md) class in your SwiftUI interface.

```swift
struct SystemPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer

    func makeUIViewController(context: Context) -> AVPlayerViewController {
        return AVPlayerViewController()
    }

    func updateUIViewController(_ avPlayerViewController: AVPlayerViewController, context: Context) {
        viewController.player = player
    }
}
```

Items will be donated to media players (like [`AVPlayerViewController`](../../AVKit/avplayerviewcontroller.md)) downstream in the hierarchy.

> **Note**: View the sample code in [Building an immersive media viewing experience](../../visionOS/building-an-immersive-media-viewing-experience.md) to see an immersive space in action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/immersiveenvironmentpicker(content:))*