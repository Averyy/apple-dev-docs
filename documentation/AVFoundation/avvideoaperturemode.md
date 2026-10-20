# AVVideoApertureMode

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A value that describes how a video is scaled or cropped.

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
struct AVVideoApertureMode
```

```c
typedef NSString * AVVideoApertureMode;
```

## Topics

### Aperture modes
- [static let cleanAperture: AVVideoApertureMode](./avvideoaperturemode/cleanaperture.md)
  The pixel aspect ratio and clean aperture will be applied.
- [static let encodedPixels: AVVideoApertureMode](./avvideoaperturemode/encodedpixels.md)
  The encoded dimensions of the image description are displayed.
- [static let productionAperture: AVVideoApertureMode](./avvideoaperturemode/productionaperture.md)
  The pixel aspect ratio will be applied.
### Initializers
- [init(rawValue: String)](./avvideoaperturemode/init%28rawvalue%29.md)
  Creates a video aperture mode with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring presentation
- [var presentationSize: CGSize](./avplayeritem/presentationsize.md)
  The size at which the visual portion of the item is presented by the player.
- [var preferredMaximumResolution: CGSize](./avplayeritem/preferredmaximumresolution.md)
  The desired maximum resolution of a video that is to be downloaded.
- [var videoApertureMode: AVVideoApertureMode](./avplayeritem/videoaperturemode.md)
  The video aperture mode to apply during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoaperturemode)*