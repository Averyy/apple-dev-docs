# VideoPlayer

**Framework**: AVKit  
**Kind**: struct

A view that displays content from a player and a native user interface to control playback.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency struct VideoPlayer<VideoOverlay> where VideoOverlay : View
```

#### Overview

```swift
import SwiftUI
import AVKit

struct ContentView: View {

    /// An optional player the view creates in a task modifier.
    ///
    /// Creating the player instance indirectly helps to avoid 
    /// performance issues and other side effects.
    @State private var player: AVPlayer?
    @State private var isPlaying = false

    var body: some View {
        VStack {
            if let player {
                VideoPlayer(player: player)
                    .frame(width: 320, height: 180, alignment: .center)

                Button {
                    isPlaying ? player.pause() : player.play()
                    isPlaying.toggle()
                    player.seek(to: .zero)
                } label: {
                    Image(systemName: isPlaying ? "stop" : "play")
                        .padding()
                }
            }
        }
        .task {
            // Use the task modifier to defer creating the player to ensure
            // SwiftUI creates it only once when it first presents the view.
            let url = // URL to local or remote media.
            player = AVPlayer(url: url)
        }
    }
}
```

## Topics

### Creating a video player
- [init(player: AVPlayer?)](videoplayer/init(player:).md)
  Creates a video-player user interface for the player object.
- [init(player: AVPlayer?, videoOverlay: () -> VideoOverlay)](videoplayer/init(player:videooverlay:).md)
  Creates a video-player user interface for the player object.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)

## See Also

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [Customizing the tvOS playback experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVPlayerView](avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewDelegate](avplayerviewdelegate.md)
  A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/videoplayer)*