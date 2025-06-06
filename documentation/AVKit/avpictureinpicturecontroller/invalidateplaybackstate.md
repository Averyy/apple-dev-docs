# invalidatePlaybackState()

**Framework**: AVKit  
**Kind**: method

Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func invalidatePlaybackState()
```

#### Discussion

Call this method whenever you start or pause playback and when the underlying content duration changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/invalidateplaybackstate())*