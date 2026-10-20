# TVMediaItemContentConfiguration

**Framework**: TVUIKit  
**Kind**: struct  
**Role**: Structure

A content configuration for a media item view.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
struct TVMediaItemContentConfiguration
```

## Topics

### Creating Default Configurations
- [static func wideCell() -> TVMediaItemContentConfiguration](./tvmediaitemcontentconfiguration-swift.struct/widecell%28%29.md)
  Creates the default configuration for a wide media item cell.
### Customizing Content
- [var image: UIImage?](./tvmediaitemcontentconfiguration-swift.struct/image.md)
  The image to display.
- [var text: String?](./tvmediaitemcontentconfiguration-swift.struct/text.md)
  The primary text.
- [var secondaryText: String?](./tvmediaitemcontentconfiguration-swift.struct/secondarytext.md)
  The secondary text.
- [var badgeText: String?](./tvmediaitemcontentconfiguration-swift.struct/badgetext.md)
  The text to display in a badge in the top corner of the content.
- [var badgeProperties: TVMediaItemContentConfiguration.BadgeProperties](./tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.property.md)
  Properties for configuring the badge.
- [TVMediaItemContentConfiguration.BadgeProperties](./tvmediaitemcontentconfiguration-swift.struct/badgeproperties-swift.struct.md)
  Properties that affect the media item content badge.
- [var overlayView: UIView?](./tvmediaitemcontentconfiguration-swift.struct/overlayview.md)
  An overlay view the system places above the image and automatically resizes to fill the frame.
- [var playbackProgress: Float](./tvmediaitemcontentconfiguration-swift.struct/playbackprogress.md)
  The playback progress to display for the media item.
### Customizing Appearance
- [TVMediaItemContentConfiguration.TextProperties](./tvmediaitemcontentconfiguration-swift.struct/textproperties-swift.struct.md)
  Properties that affect the media item content configuration’s text.
- [var textProperties: TVMediaItemContentConfiguration.TextProperties](./tvmediaitemcontentconfiguration-swift.struct/textproperties-swift.property.md)
  Properties for configuring the primary text.
- [var secondaryTextProperties: TVMediaItemContentConfiguration.TextProperties](./tvmediaitemcontentconfiguration-swift.struct/secondarytextproperties.md)
  Properties for configuring the secondary text.
### Creating a Content View
- [func makeContentView() -> any UIView & UIContentView](./tvmediaitemcontentconfiguration-swift.struct/makecontentview%28%29.md)
  Creates a new instance of the content view using this configuration.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [UIContentConfiguration](../UIKit/uicontentconfiguration-9eib5.md)

## See Also

### Creating a Media Item Content View
- [convenience init(configuration: TVMediaItemContentConfiguration)](./tvmediaitemcontentview/init%28configuration%29.md)
  Creates a media item content view with the configuration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentconfiguration-swift.struct)*