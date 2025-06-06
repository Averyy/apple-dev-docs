# setMagnification(_:centeredAt:)

**Framework**: AVKit  
**Kind**: method

Scales the video’s view by a specified factor, and centers the result on a specified point.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func setMagnification(_ magnification: CGFloat, centeredAt point: CGPoint)
```

#### Discussion

The supported magnification range is `1.0` to `64.0`. The system zooms using nearest neighbor interpolation after it scales the content past a certain factor.

## Parameters

- `magnification`: A factor by which to scale the video’s view.
- `point`: A point in view space on which to center magnification.

## See Also

- [var allowsMagnification: Bool](avplayerview/allowsmagnification.md)
  A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.
- [var magnification: CGFloat](avplayerview/magnification.md)
  The factor by which the video’s view is currently scaled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/setmagnification(_:centeredat:))*