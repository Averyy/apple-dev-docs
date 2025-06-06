# allowsMagnification

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var allowsMagnification: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). This property only affects whether the magnify gesture triggers magnification. Your app can still programmatically change magnification even when the value of this is [`false`](https://developer.apple.com/documentation/swift/false), which matches the behavior of [`NSScrollView`](https://developer.apple.com/documentation/AppKit/NSScrollView).

## See Also

- [var magnification: CGFloat](avplayerview/magnification.md)
  The factor by which the video’s view is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](avplayerview/setmagnification(_:centeredat:).md)
  Scales the video’s view by a specified factor, and centers the result on a specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/allowsmagnification)*