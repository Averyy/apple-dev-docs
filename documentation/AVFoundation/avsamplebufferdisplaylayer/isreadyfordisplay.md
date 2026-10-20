# isReadyForDisplay

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the first video frame is ready for display.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var isReadyForDisplay: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isReadyForDisplay) BOOL readyForDisplay;
```

## See Also

### Configuring the layer
- [var controlTimebase: CMTimebase?](./controltimebase.md)
  A timebase that determines how the layer interprets timestamps.
- [var videoGravity: AVLayerVideoGravity](./videogravity.md)
  A value that indicates how the layer displays video within its bounds.
- [struct AVLayerVideoGravity](../avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/isreadyfordisplay)*