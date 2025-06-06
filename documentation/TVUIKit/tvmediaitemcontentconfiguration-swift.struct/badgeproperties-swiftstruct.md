# TVMediaItemContentConfiguration.BadgeProperties

**Framework**: TVUIKit  
**Kind**: struct

Properties that affect the media item content badge.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
struct BadgeProperties
```

## Topics

### Creating a Default Configuration
- [static func `default`() -> TVMediaItemContentConfiguration.BadgeProperties](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct/default.md)
  Creates the default configuration for a badge.
- [static func liveContent() -> TVMediaItemContentConfiguration.BadgeProperties](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct/livecontent.md)
  Creates the default configuration for a badge representing live content.
### Customizing Content
- [var font: UIFont](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct/font.md)
  The font for the badge text.
- [var color: UIColor](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct/color.md)
  The color of the badge text.
- [var backgroundColor: UIColor](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct/backgroundcolor.md)
  The background tint color of the badge.
- [var transform: TVMediaItemContentConfiguration.TextProperties.TextTransform](tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct/transform.md)
  The transform to apply to the text before displaying it.
- [TVMediaItemContentConfiguration.TextProperties.TextTransform](tvmediaitemcontentconfiguration-swift.struct/textproperties-swift.struct/texttransform.md)
  Constants that specify the transform to apply to the text.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [var overlayView: UIView?](tvmediaitemcontentconfiguration-swift.struct/overlayview.md)
  An overlay view the system places above the image and automatically resizes to fill the frame.
- [var playbackProgress: Float](tvmediaitemcontentconfiguration-swift.struct/playbackprogress.md)
  The playback progress to display for the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct)*