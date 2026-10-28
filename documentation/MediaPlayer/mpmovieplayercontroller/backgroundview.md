# backgroundView

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A customizable view that is displayed behind the movie content.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var backgroundView: UIView! { get }
```

```objc
@property (nonatomic, readonly) UIView * backgroundView;
```

## Discussion

This view provides the backing content, on top of which the movie content is displayed. You can add subviews to the background view if you want to display custom background content.

This view is part of the view hierarchy returned by the [`view`](./view.md) property.

## See Also

### Accessing the view
- [var view: UIView!](./view.md)
  The view containing the movie content and controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/backgroundview)*