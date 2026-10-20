# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The transform performed on the visual media data of the track for display purposes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preferredTransform: CGAffineTransform { get set }
```

```objc
@property (nonatomic) CGAffineTransform preferredTransform;
```

## See Also

### Accessing visual characteristics
- [var naturalSize: CGSize](./naturalsize.md)
  The dimensions used to display the visual media data for the track.
- [var layer: Int](./layer.md)
  The layer level for the visual media of the track.
- [var cleanApertureDimensions: CGSize](./cleanaperturedimensions.md)
  The clean aperture dimension of the track.
- [var productionApertureDimensions: CGSize](./productionaperturedimensions.md)
  The production aperture dimensions of the track.
- [var encodedPixelsDimensions: CGSize](./encodedpixelsdimensions.md)
  The encoded pixels dimensions of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/preferredtransform)*