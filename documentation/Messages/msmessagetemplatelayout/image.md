# image

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

An image used to represent the message in the transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * image;
```

## Discussion

The system crops the left and right edges of the image by 6 points, and rounds the image’s corners.

The template can have either an image or a media file. If this property is set to a non-`nil` value, the [`mediaFileURL`](./mediafileurl.md) property is ignored. This property defaults to `nil`.

## See Also

### Assigning Visual Elements
- [var mediaFileURL: URL?](./mediafileurl.md)
  A media file used to represent the message in the transcript.
- [var imageTitle: String?](./imagetitle.md)
  The title for the image or media file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/image)*