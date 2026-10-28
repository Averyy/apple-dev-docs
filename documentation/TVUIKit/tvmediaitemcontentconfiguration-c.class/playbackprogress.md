# playbackProgress

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The playback progress to display for the media item.

**Availability**:
- tvOS 15.0+

## Declaration

```objc
@property (nonatomic, assign) float playbackProgress;
```

## Discussion

The system clamps the value between `0.0` and `1.0`.

## See Also

### Customizing Content
- [image](./image.md)
  The image to display.
- [text](./text.md)
  The primary text.
- [secondaryText](./secondarytext.md)
  The secondary text.
- [badgeText](./badgetext.md)
  The text to display in a badge in the top corner of the content.
- [badgeProperties](./badgeproperties.md)
  Properties for configuring the badge.
- [TVMediaItemContentBadgeProperties](../tvmediaitemcontentbadgeproperties.md)
  Properties that affect the media item content badge.
- [overlayView](./overlayview.md)
  An overlay view the system places above the image and automatically resizes to fill the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentconfiguration-c.class/playbackprogress)*