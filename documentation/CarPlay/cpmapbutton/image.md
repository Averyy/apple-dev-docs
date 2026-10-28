# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image to display on the button.

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

This property doesn’t support animated images. If it’s set with an animated image, the button displays the first image in the animated sequence.

## See Also

### Providing Button Images
- [var focusedImage: UIImage?](./focusedimage.md)
  The image to display when focus is on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton/image)*