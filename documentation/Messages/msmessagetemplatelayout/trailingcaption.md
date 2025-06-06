# trailingCaption

**Framework**: Messages  
**Kind**: property

A right-aligned caption for the message bubble.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var trailingCaption: String? { get set }
```

#### Discussion

The trailing caption is drawn using black text and is positioned at the bottom-right corner of the message bubble, just below the image or media file. This text is right aligned and positioned on the same line as the caption. The trailing caption can wrap to three lines before being truncated. This property defaults to `nil`.

## See Also

- [var image: UIImage?](msmessagetemplatelayout/image.md)
  An image used to represent the message in the transcript.
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
- [var trailingSubcaption: String?](msmessagetemplatelayout/trailingsubcaption.md)
  A right-aligned subcaption for the message bubble.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/trailingcaption)*