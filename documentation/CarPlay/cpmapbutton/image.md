# image

**Framework**: CarPlay  
**Kind**: property

The image to display on the button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var image: UIImage? { get set }
```

#### Discussion

This property doesn’t support animated images. If it’s set with an animated image, the button displays the first image in the animated sequence.

## See Also

- [var focusedImage: UIImage?](cpmapbutton/focusedimage.md)
  The image to display when focus is on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton/image)*