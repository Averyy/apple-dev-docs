# title

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The title displayed on the bar button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

## Discussion

Setting this property has an effect only when the button type is [`CPBarButton.Type.text`](./type/text.md).

## See Also

### Configuring the Button
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that enables and disables the bar button.
- [var image: UIImage?](./image.md)
  The image displayed on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/title)*