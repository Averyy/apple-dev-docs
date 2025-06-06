# Implementing simple enhanced buffering for your content

**Framework**: AVFoundation

Configure your app for simple enhanced buffering to stream content faster to AirPlay-enabled devices and supported CarPlay vehicles.

#### Overview

The [`AVPlayer`](avplayer.md) and [`AVQueuePlayer`](avqueueplayer.md) classes provide the simplest way to enhance buffering for your content with AirPlay 2.

To implement simple enhanced buffering, complete the following steps.

1. Create a player.

```swift
let player = AVQueuePlayer()
```

1. Identify a URL that points to local or cloud content that you want to play.
2. Create an [`AVAsset`](avasset.md) instance with a URL, and then create an [`AVPlayerItem`](avplayeritem.md) instance with that asset.

```swift
let url = URL(string: "http://www.examplecontenturl.com")!
let asset = AVAsset(url: url)
let item = AVPlayerItem(asset: asset)
```

1. Give the player item to the player.

```swift
player.insert(item, after: nil)
```

1. Start playback.

```swift
player.play()
```

## See Also

- [Implementing flexible enhanced buffering for your content](implementing-flexible-enhanced-buffering-for-your-content.md)
  Configure your app for flexible enhanced buffering to stream content faster to AirPlay-enabled devices and supported CarPlay vehicles.
- [Integrating AirPlay for Long-Form Video Apps](integrating-airplay-for-long-form-video-apps.md)
  Integrate AirPlay features and implement a dedicated external playback experience by preparing the routing system for long-form video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/implementing-simple-enhanced-buffering-for-your-content)*