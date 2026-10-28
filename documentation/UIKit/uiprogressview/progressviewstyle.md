# progressViewStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current graphical style of the progress view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var progressViewStyle: UIProgressView.Style { get set }
```

```objc
@property (nonatomic) UIProgressViewStyle progressViewStyle;
```

## Discussion

The value of this property is a constant that specifies the style of the progress view. The default style is [`UIProgressView.Style.default`](./style/default.md). For more on these constants, see [`UIProgressView.Style`](./style.md).

## See Also

### Configuring the progress bar
- [var progressTintColor: UIColor?](./progresstintcolor.md)
  The color shown for the portion of the progress bar that’s filled.
- [var progressImage: UIImage?](./progressimage.md)
  An image to use for the portion of the progress bar that’s filled.
- [var trackTintColor: UIColor?](./tracktintcolor.md)
  The color shown for the portion of the progress bar that isn’t filled.
- [var trackImage: UIImage?](./trackimage.md)
  An image to use for the portion of the track that isn’t filled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/progressviewstyle)*