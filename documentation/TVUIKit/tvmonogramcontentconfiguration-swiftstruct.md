# TVMonogramContentConfiguration

**Framework**: TVUIKit  
**Kind**: struct

A content configuration for a monogram view.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
struct TVMonogramContentConfiguration
```

## Topics

### Creating Default Configurations
- [static func cell() -> TVMonogramContentConfiguration](tvmonogramcontentconfiguration-swift.struct/cell.md)
  Creates the default configuration for a circular monogram cell.
### Customizing Content
- [var image: UIImage?](tvmonogramcontentconfiguration-swift.struct/image.md)
  The image to display.
- [var text: String?](tvmonogramcontentconfiguration-swift.struct/text.md)
  The primary text.
- [var secondaryText: String?](tvmonogramcontentconfiguration-swift.struct/secondarytext.md)
  The secondary text.
- [var personNameComponents: PersonNameComponents?](tvmonogramcontentconfiguration-swift.struct/personnamecomponents.md)
  The name the system uses when creating a monogram image.
### Customizing Appearance
- [var textProperties: TVMonogramContentConfiguration.TextProperties](tvmonogramcontentconfiguration-swift.struct/textproperties-swift.property.md)
  Properties for configuring the primary text.
- [var secondaryTextProperties: TVMonogramContentConfiguration.TextProperties](tvmonogramcontentconfiguration-swift.struct/secondarytextproperties.md)
  Properties for configuring the secondary text.
- [TVMonogramContentConfiguration.TextProperties](tvmonogramcontentconfiguration-swift.struct/textproperties-swift.struct.md)
  Properties that affect the monogram content configuration’s text.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [UIContentConfiguration](../uikit/uicontentconfiguration-9eib5.md)

## See Also

- [convenience init(configuration: TVMonogramContentConfiguration)](tvmonogramcontentview/init(configuration:).md)
  Creates a monogram content view with the configuration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentconfiguration-swift.struct)*