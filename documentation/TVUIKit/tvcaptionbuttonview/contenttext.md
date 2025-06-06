# contentText

**Framework**: TVUIKit  
**Kind**: property

The text displayed in the main content view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var contentText: String? { get set }
```

#### Discussion

The content text is displayed in the caption button and indicates the purpose of the caption button. The last instance of [`contentImage`](tvcaptionbuttonview/contentimage.md) or [`contentText`](tvcaptionbuttonview/contenttext.md) that was set in your app is displayed by the caption button view.

## See Also

- [var contentImage: UIImage?](tvcaptionbuttonview/contentimage.md)
  The image displayed in the main content view.
- [var title: String?](tvcaptionbuttonview/title.md)
  The title for the caption button.
- [var subtitle: String?](tvcaptionbuttonview/subtitle.md)
  The subtitle of the caption button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview/contenttext)*