# magnification

**Framework**: AVKit  
**Kind**: property

The factor by which the video’s view is currently scaled.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var magnification: CGFloat { get set }
```

#### Discussion

The supported magnification range is `1.0` to `64.0`. The system zooms using nearest neighbor interpolation after it scales the content past a certain factor.

The default value is `1.0`.

## See Also

- [var allowsMagnification: Bool](avplayerview/allowsmagnification.md)
  A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](avplayerview/setmagnification(_:centeredat:).md)
  Scales the video’s view by a specified factor, and centers the result on a specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/magnification)*