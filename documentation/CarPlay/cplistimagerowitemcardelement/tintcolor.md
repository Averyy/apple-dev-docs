# tintColor

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The color to use for the card’s background.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@NSCopying
var tintColor: UIColor? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIColor * tintColor;
```

## Discussion

When the value in the `showsImageFullHeight` property is `false`, CarPlay fills the card shape with this color before layering the image and text on top of the card. When the value in `showsImageFullHeight` is `true`, CarPlay applies the tint color behind the labels at the bottom of the card.

If the value in this property is `nil`, CarPlay uses the [`secondarySystemBackground`](../../UIKit/uicolor/secondarysystembackground.md) color.

## See Also

### Getting the element’s content
- [var title: String](./title.md)
  The primary text for the element.
- [var subtitle: String?](./subtitle.md)
  The secondary text for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/tintcolor)*