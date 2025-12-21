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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/videoplayer)*