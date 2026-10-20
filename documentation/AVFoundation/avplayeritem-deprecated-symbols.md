# Deprecated symbols

**Framework**: AVFoundation  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Accessing metadata
- [var timedMetadata: [AVMetadataItem]?](./avplayeritem/timedmetadata.md)
  An array of the most recently encountered timed metadata.
### Seeking through media
- [func seek(to: CMTime)](./avplayeritem/seek%28to%29-1dpto.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](./avplayeritem/seek%28to,tolerancebefore,toleranceafter%29.md)
  Sets the current playback time within a specified time bound.
- [func seek(to: Date) async -> Bool](./avplayeritem/seek%28to%29-5rt4x.md)
  Sets the current playback time to the time specified by the date object.
- [func seek(to: Date) -> Bool](./avplayeritem/seek%28to%29-3s9d8.md)
  Sets the current playback time to the time specified by the date object.
### Selecting media options
- [func selectedMediaOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](./avplayeritem/selectedmediaoption%28in%29.md)
  Returns the media selection option that’s currently selected from the specified group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem-deprecated-symbols)*