# image

**Framework**: CarPlay  
**Kind**: property

The image displayed on the bar button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage? { get set }
```

#### Discussion

If you provide an animated image, the button displays only the first image in the animation sequence.

Setting this property has an effect only when the button type is [`CPBarButton.Type.image`](cpbarbutton/type/image.md).

## See Also

- [var isEnabled: Bool](cpbarbutton/isenabled.md)
  A Boolean value that enables and disables the bar button.
- [var title: String?](cpbarbutton/title.md)
  The title displayed on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/image)*