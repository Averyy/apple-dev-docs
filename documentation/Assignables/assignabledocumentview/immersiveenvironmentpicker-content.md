# immersiveEnvironmentPicker(content:)

**Framework**: Assignables  
**Kind**: method

Add menu items to open immersive spaces from a media player’s environment picker.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func immersiveEnvironmentPicker<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

These items are added alongside recently used system environments.

```None
SystemPlayerView(player: player)
    .immersiveEnvironmentPicker {
        Button("Chalet", systemImage: "fireplace") {
            Task {
                await openImmersiveSpace(id: "Chalet")
            }
        }
    }
```

Use a `UIViewControllerRepresentable` instance to display a [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) class in your SwiftUI interface.

```None
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

Items will be donated to media players (like [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController)) downstream in the hierarchy.

> **Note**: View the sample code in [`Building an immersive media viewing experience`](https://developer.apple.com/documentation/visionOS/building-an-immersive-media-viewing-experience) to see an immersive space in action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/immersiveenvironmentpicker(content:))*