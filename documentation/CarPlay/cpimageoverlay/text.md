# text

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The text to display in a badge at the top of the thumbnail.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var text: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * text;
```

## Discussion

Specify the text to display at initialization time. The text appears on a badge background using the colors you specified and with the placement in the [`alignment`](./alignment-swift.property.md) property. If you initialized the overlay with an image, the value in this property is `nil`.

## See Also

### Getting the overlay details
- [var image: UIImage?](./image.md)
  The image to display at top of the thumbnail.
- [var textColor: UIColor?](./textcolor.md)
  The color to apply to the badge’s text.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color to display behind the badge’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay/text)*