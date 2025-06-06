# progressViewStyle

**Framework**: UIKit  
**Kind**: property

The current graphical style of the progress view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var progressViewStyle: UIProgressView.Style { get set }
```

#### Discussion

The value of this property is a constant that specifies the style of the progress view. The default style is [`UIProgressView.Style.default`](uiprogressview/style/default.md). For more on these constants, see [`UIProgressView.Style`](uiprogressview/style.md).

## See Also

- [var progressTintColor: UIColor?](uiprogressview/progresstintcolor.md)
  The color shown for the portion of the progress bar that’s filled.
- [var progressImage: UIImage?](uiprogressview/progressimage.md)
  An image to use for the portion of the progress bar that’s filled.
- [var trackTintColor: UIColor?](uiprogressview/tracktintcolor.md)
  The color shown for the portion of the progress bar that isn’t filled.
- [var trackImage: UIImage?](uiprogressview/trackimage.md)
  An image to use for the portion of the track that isn’t filled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/progressviewstyle)*