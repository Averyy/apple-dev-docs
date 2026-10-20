# TVMediaItemContentConfiguration.BadgeProperties

**Framework**: TVUIKit  
**Kind**: struct  
**Role**: Structure

Properties that affect the media item content badge.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
struct BadgeProperties
```

## Topics

### Creating a Default Configuration
- [static func `default`() -> TVMediaItemContentConfiguration.BadgeProperties](./badgeproperties-swift.struct/default%28%29.md)
  Creates the default configuration for a badge.
- [static func liveContent() -> TVMediaItemContentConfiguration.BadgeProperties](./badgeproperties-swift.struct/livecontent%28%29.md)
  Creates the default configuration for a badge representing live content.
### Customizing Content
- [var font: UIFont](./badgeproperties-swift.struct/font.md)
  The font for the badge text.
- [var color: UIColor](./badgeproperties-swift.struct/color.md)
  The color of the badge text.
- [var backgroundColor: UIColor](./badgeproperties-swift.struct/backgroundcolor.md)
  The background tint color of the badge.
- [var transform: TVMediaItemContentConfiguration.TextProperties.TextTransform](./badgeproperties-swift.struct/transform.md)
  The transform to apply to the text before displaying it.
- [TVMediaItemContentConfiguration.TextProperties.TextTransform](./textproperties-swift.struct/texttransform.md)
  Constants that specify the transform to apply to the text.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../../Swift/customreflectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

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
- [var overlayView: UIView?](./overlayview.md)
  An overlay view the system places above the image and automatically resizes to fill the frame.
- [var playbackProgress: Float](./playbackprogress.md)
  The playback progress to display for the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct)*