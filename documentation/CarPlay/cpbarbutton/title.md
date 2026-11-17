# title

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The text to display in the button.

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

Specify the button’s text at initialization time and use this property to update it. If you initialize the button with an image instead of text, this property is `nil`.

## See Also

### Configuring the button
- [var image: UIImage?](./image.md)
  The image to display in the button.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the button is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/title)*