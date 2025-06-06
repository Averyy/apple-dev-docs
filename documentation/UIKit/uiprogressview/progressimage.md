# progressImage

**Framework**: UIKit  
**Kind**: property

An image to use for the portion of the progress bar that’s filled.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var progressImage: UIImage? { get set }
```

#### Discussion

If you provide a custom image, the [`progressTintColor`](uiprogressview/progresstintcolor.md) property is ignored.

## See Also

- [var progressViewStyle: UIProgressView.Style](uiprogressview/progressviewstyle.md)
  The current graphical style of the progress view.
- [var progressTintColor: UIColor?](uiprogressview/progresstintcolor.md)
  The color shown for the portion of the progress bar that’s filled.
- [var trackTintColor: UIColor?](uiprogressview/tracktintcolor.md)
  The color shown for the portion of the progress bar that isn’t filled.
- [var trackImage: UIImage?](uiprogressview/trackimage.md)
  An image to use for the portion of the track that isn’t filled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/progressimage)*