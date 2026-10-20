# trackTintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color shown for the portion of the progress bar that isn’t filled.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var trackTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * trackTintColor;
```

#### Discussion

If you set [`trackTintColor`](./tracktintcolor.md) to `nil`, the track uses the tint of its parent.

## See Also

### Configuring the progress bar
- [var progressViewStyle: UIProgressView.Style](./progressviewstyle.md)
  The current graphical style of the progress view.
- [var progressTintColor: UIColor?](./progresstintcolor.md)
  The color shown for the portion of the progress bar that’s filled.
- [var progressImage: UIImage?](./progressimage.md)
  An image to use for the portion of the progress bar that’s filled.
- [var trackImage: UIImage?](./trackimage.md)
  An image to use for the portion of the track that isn’t filled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/tracktintcolor)*