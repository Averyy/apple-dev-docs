# playbackProgress

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The playback progress to display for the media item.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
var playbackProgress: Float { get set }
```

## Discussion

The system clamps the value between `0.0` and `1.0`.

## See Also

### Customizing Content
- [var image: UIImage?](./image.md)
  The image to display.
- [var text: String?](./text.md)
  The primary text.
- [var secondaryText: String?](./secondarytext.md)
  The secondary text.
- [var badgeText: String?](./badgetext.md)
  The text to display in a badge in the top corner of the content.
- [var badgeProperties: TVMediaItemContentConfiguration.BadgeProperties](./badgeproperties-swift.property.md)
  Properties for configuring the badge.
- [TVMediaItemContentConfiguration.BadgeProperties](./badgeproperties-swift.struct.md)
  Properties that affect the media item content badge.
- [var overlayView: UIView?](./overlayview.md)
  An overlay view the system places above the image and automatically resizes to fill the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentconfiguration-swift.struct/playbackprogress)*