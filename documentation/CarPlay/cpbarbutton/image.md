# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image to display in the button.

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

## Discussion

Specify the button’s image at initialization time and use this property to update it. If you initialize the button with text instead of an image, this property is `nil`.

## See Also

### Configuring the button
- [var title: String?](./title.md)
  The text to display in the button.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the button is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/image)*