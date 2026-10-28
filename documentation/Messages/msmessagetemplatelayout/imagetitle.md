# imageTitle

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The title for the image or media file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var imageTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * imageTitle;
```

## Discussion

The title is drawn using white text on the bottom-left corner of the image or media file. This property defaults to `nil`.

## See Also

### Assigning Visual Elements
- [var image: UIImage?](./image.md)
  An image used to represent the message in the transcript.
- [var mediaFileURL: URL?](./mediafileurl.md)
  A media file used to represent the message in the transcript.
- [var imageSubtitle: String?](./imagesubtitle.md)
  The subtitle for the image or media file.
- [var caption: String?](./caption.md)
  A left-aligned caption for the message bubble.
- [var subcaption: String?](./subcaption.md)
  A left-aligned subcaption for the message bubble.
- [var trailingCaption: String?](./trailingcaption.md)
  A right-aligned caption for the message bubble.
- [var trailingSubcaption: String?](./trailingsubcaption.md)
  A right-aligned subcaption for the message bubble.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/imagetitle)*