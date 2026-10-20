# contentText

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The text displayed in the main content view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var contentText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * contentText;
```

#### Discussion

The content text is displayed in the caption button and indicates the purpose of the caption button. The last instance of [`contentImage`](./contentimage.md) or [`contentText`](./contenttext.md) that was set in your app is displayed by the caption button view.

## See Also

### Configuring the Caption Button
- [var contentImage: UIImage?](./contentimage.md)
  The image displayed in the main content view.
- [var title: String?](./title.md)
  The title for the caption button.
- [var subtitle: String?](./subtitle.md)
  The subtitle of the caption button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview/contenttext)*