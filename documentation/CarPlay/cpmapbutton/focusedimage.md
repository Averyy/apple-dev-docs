# focusedImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image to display when focus is on the button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var focusedImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * focusedImage;
```

#### Discussion

If `focusedImage` is nil, the button uses [`image`](./image.md) as the default, creating a focused image using the alpha values from the image.

## See Also

### Providing Button Images
- [var image: UIImage?](./image.md)
  The image to display on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton/focusedimage)*