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
    @State var player = AVPlayer(url: Bundle.main.url(forResource: "video2",
                                                      withExtension: "m4v")!)
    @State var isPlaying: Bool = false
    
    var body: some View {
        VStack {
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