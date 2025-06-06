# mediaFileURL

**Framework**: Messages  
**Kind**: property

A media file used to represent the message in the transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mediaFileURL: URL? { get set }
```

#### Discussion

The media file URL must be a file URL. For video files, the system crops the left and right edges of the media file by 6 points, and rounds its corners. For audio files, it shows a graphical representation of the audio’s waveform.

The template can have either an image or a media file. This property is ignored if the template has a non-`nil` [`image`](msmessagetemplatelayout/image.md) property. This property defaults to `nil`.

## See Also

- [var image: UIImage?](msmessagetemplatelayout/image.md)
  An image used to represent the message in the transcript.
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

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/mediafileurl)*