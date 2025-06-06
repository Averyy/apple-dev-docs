# playbackProgress

**Framework**: TVUIKit  
**Kind**: property

The playback progress to display for the media item.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
var playbackProgress: Float { get set }
```

#### Discussion

The system clamps the value between `0.0` and `1.0`.

## See Also

- [var image: UIImage?](tvmediaitemcontentconfiguration-swift.struct/image.md)
  The image to display.
- [var text: String?](tvmediaitemcontentconfiguration-swift.struct/text.md)
  The primary text.
- [var secondaryText: String?](tvmediaitemcontentconfiguration-swift.struct/secondarytext.md)
  The secondary text.
- [var badgeText: String?](tvmediaitemcontentconfiguration-swift.struct/badgetext.md)
  The text to display in a badge in the top corner of the content.
- [var badgeProperties: TVMediaItemContentConfiguration.BadgeProperties](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.property.md)
  Properties for configuring the badge.
- [TVMediaItemContentConfiguration.BadgeProperties](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct.md)
  Properties that affect the media item content badge.
- [var overlayView: UIView?](tvmediaitemcontentconfiguration-swift.struct/overlayview.md)
  An overlay view the system places above the image and automatically resizes to fill the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentconfiguration-swift.struct/playbackprogress)*