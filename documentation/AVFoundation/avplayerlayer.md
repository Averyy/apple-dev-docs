# AVPlayerLayer

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that presents the visual contents of a player object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlayerLayer
```

```objc
@interface AVPlayerLayer : CALayer
```

## Mentions

- [Selecting subtitles and alternative audio tracks](./selecting-subtitles-and-alternative-audio-tracks.md)

#### Overview

A common way to use this object in iOS or tvOS is as the backing layer for a [`UIView`](../UIKit/uiview.md), as the following example shows:

```swift
/// A view that displays the visual contents of a player object.
class PlayerView: UIView {

    // Override the property to make AVPlayerLayer the view's backing layer.
    override static var layerClass: AnyClass { AVPlayerLayer.self }
    
    // The associated player object.
    var player: AVPlayer? {
        get { playerLayer.player }
        set { playerLayer.player = newValue }
    }
    
    private var playerLayer: AVPlayerLayer { layer as! AVPlayerLayer }
}
```

> ❗ **Important**:  The value of a player layer’s inherited [`contents`](../QuartzCore/calayer/contents.md) property is opaque and you can’t change it.

## Topics

### Creating a player layer
- [init(player: AVPlayer?)](./avplayerlayer/init%28player%29.md)
  Creates a layer object to present the visual contents of a player’s current item.
### Configuring the presentation
- [var videoRect: CGRect](./avplayerlayer/videorect.md)
  The current size and position of the video image that displays within the layer’s bounds.
- [var videoGravity: AVLayerVideoGravity](./avplayerlayer/videogravity.md)
  A value that specifies how the layer displays the player’s visual content within the layer’s bounds.
- [struct AVLayerVideoGravity](./avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.
### Determining display readiness
- [var isReadyForDisplay: Bool](./avplayerlayer/isreadyfordisplay.md)
  A Boolean value that indicates whether the first video frame of the player’s current item is ready for display.
### Accessing the player
- [var player: AVPlayer?](./avplayerlayer/player.md)
  The player whose visual content the layer displays.
### Processing pixel buffers
- [var pixelBufferAttributes: [String : Any]?](./avplayerlayer/pixelbufferattributes.md)
  The attributes of the visual output that displays in the player layer during playback.
- [func displayedPixelBuffer() -> CVPixelBuffer?](./avplayerlayer/displayedpixelbuffer%28%29.md)
  Returns the pixel buffer that the player layer currently displays.
- [func displayedReadOnlyPixelBuffer() -> CVReadOnlyPixelBuffer?](./avplayerlayer/displayedreadonlypixelbuffer%28%29.md)
  Returns the pixel buffer which is currently being displayed.
### Instance Methods
- [func setCaptionPreviewProfileID(String, position: CGPoint, text: String?)](./avplayerlayer/setcaptionpreviewprofileid%28_,position,text%29.md)
  Starts displaying a caption preview with the specified accessibility profile.
- [func stopShowingCaptionPreview()](./avplayerlayer/stopshowingcaptionpreview%28%29.md)
  Stops showing the caption preview.

## Relationships

### Inherits From
- [CALayer](../QuartzCore/calayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Presentation
- [Monitoring playback progress in your app](./monitoring-playback-progress-in-your-app.md)
  Observe the playback of a media asset to update your app’s user-interface state.
- [Using HEVC video with alpha](./using-hevc-video-with-alpha.md)
  Play, write, and export HEVC video with an alpha channel to add overlay effects to your video processing.
- [class AVSynchronizedLayer](./avsynchronizedlayer.md)
  A Core Animation layer that derives its timing from a player item so that you can synchronize layer animations with media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer)*