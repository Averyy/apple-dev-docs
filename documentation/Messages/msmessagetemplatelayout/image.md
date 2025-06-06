# image

**Framework**: Messages  
**Kind**: property

An image used to represent the message in the transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage? { get set }
```

#### Discussion

The system crops the left and right edges of the image by 6 points, and rounds the image’s corners.

The template can have either an image or a media file. If this property is set to a non-`nil` value, the [`mediaFileURL`](msmessagetemplatelayout/mediafileurl.md) property is ignored. This property defaults to `nil`.

## See Also

- [var mediaFileURL: URL?](msmessagetemplatelayout/mediafileurl.md)
  A media file used to represent the message in the transcript.
- [var imageTitle: String?](msmessagetemplatelayout/imagetitle.md)
  The title for the image or media file.
- [var imageSubtitle: String?](msmessagetemplatelayout/imagesubtitle.md)
  The subtitle for the image or media file.
- [var caption: String?](msmessagetemplatelayout/caption.md)
  A left-aligned caption for the message bubble.
- [var subcaption: String?](msmessagetemplatelayout/subcaption.md)
  A left-aligned subcaption for the message bubble.
- [var trailingCaption: String?](msmessagetemplatelayout/trailingcaption.md)
  A right-aligned caption for the message bubble.
- [var trailingSubcaption: String?](msmessagetemplatelayout/trailingsubcaption.md)
  A right-aligned subcaption for the message bubble.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/image)*