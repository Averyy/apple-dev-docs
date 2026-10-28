# presentationSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The size at which the visual portion of the item is presented by the player.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
var presentationSize: CGSize { get }
```

```objc
@property (readonly) CGSize presentationSize;
```

## Discussion

This property can be accessed at any time, but may return a value of `CGSizeZero` prior to the player item becoming ready to play. You can use key-value observing to obtain the player item’s valid presentation size as early as possible.

## See Also

### Configuring presentation
- [var preferredMaximumResolution: CGSize](./preferredmaximumresolution.md)
  The desired maximum resolution of a video that is to be downloaded.
- [var videoApertureMode: AVVideoApertureMode](./videoaperturemode.md)
  The video aperture mode to apply during playback.
- [struct AVVideoApertureMode](../avvideoaperturemode.md)
  A value that describes how a video is scaled or cropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/presentationsize)*