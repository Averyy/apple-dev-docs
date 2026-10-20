# trailingSubcaption

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

A right-aligned subcaption for the message bubble.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var trailingSubcaption: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * trailingSubcaption;
```

#### Discussion

The trailing subcaption is drawn using gray text, and is positioned below the trailing caption. This text is right aligned and positioned on the same line as the subcaption. This property defaults to `nil`.

## See Also

### Assigning Visual Elements
- [var image: UIImage?](./image.md)
  An image used to represent the message in the transcript.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/trailingsubcaption)*