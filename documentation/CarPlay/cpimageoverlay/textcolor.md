# textColor

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The color to apply to the badge’s text.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var textColor: UIColor? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIColor * textColor;
```

## Discussion

Specify the text color at initialization time.  If you initialized the overlay with an image, the value in this property is `nil`.

## See Also

### Getting the overlay details
- [var image: UIImage?](./image.md)
  The image to display at top of the thumbnail.
- [var text: String?](./text.md)
  The text to display in a badge at the top of the thumbnail.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color to display behind the badge’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay/textcolor)*