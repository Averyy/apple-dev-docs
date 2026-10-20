# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image displayed on the bar button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * image;
```

#### Discussion

If you provide an animated image, the button displays only the first image in the animation sequence.

Setting this property has an effect only when the button type is [`CPBarButton.Type.image`](./type/image.md).

## See Also

### Configuring the Button
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that enables and disables the bar button.
- [var title: String?](./title.md)
  The title displayed on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/image)*