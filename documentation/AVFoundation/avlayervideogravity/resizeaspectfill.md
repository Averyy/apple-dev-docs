# resizeAspectFill

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The video preserves its aspect ratio and fills the layer’s bounds.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let resizeAspectFill: AVLayerVideoGravity
```

```c
extern AVLayerVideoGravity const AVLayerVideoGravityResizeAspectFill;
```

#### Discussion

This gravity value may crop the video image along its horizontal or vertical dimension.

## See Also

### Video gravities
- [static let resize: AVLayerVideoGravity](./resize.md)
  The video stretches to fill the layer’s bounds.
- [static let resizeAspect: AVLayerVideoGravity](./resizeaspect.md)
  The video preserves its aspect ratio and fits it within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avlayervideogravity/resizeaspectfill)*