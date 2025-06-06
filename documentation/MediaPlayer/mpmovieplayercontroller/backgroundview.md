# backgroundView

**Framework**: Media Player  
**Kind**: property

A customizable view that is displayed behind the movie content.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var backgroundView: UIView! { get }
```

#### Discussion

This view provides the backing content, on top of which the movie content is displayed. You can add subviews to the background view if you want to display custom background content.

This view is part of the view hierarchy returned by the [`view`](mpmovieplayercontroller/view.md) property.

## See Also

- [var view: UIView!](mpmovieplayercontroller/view.md)
  The view containing the movie content and controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/backgroundview)*