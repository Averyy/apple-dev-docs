# CPDashboardButton

**Framework**: CarPlay  
**Kind**: class

A shortcut button for placement on the CarPlay Dashboard.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class CPDashboardButton
```

## Topics

### Creating a Dashboard Button
- [init(titleVariants: [String], subtitleVariants: [String], image: UIImage, handler: ((CPDashboardButton) -> Void)?)](cpdashboardbutton/init(titlevariants:subtitlevariants:image:handler:).md)
  Creates a dashboard button that displays a title, an optional subtitle, and an image.
### Accessing the Button Configuration
- [var titleVariants: [String]](cpdashboardbutton/titlevariants.md)
  The array of title variants for the button.
- [var subtitleVariants: [String]](cpdashboardbutton/subtitlevariants.md)
  The array of subtitle variants for the button.
- [var image: UIImage](cpdashboardbutton/image.md)
  The image the button displays.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var shortcutButtons: [CPDashboardButton]](cpdashboardcontroller/shortcutbuttons.md)
  An array of shortcut buttons to display on the CarPlay Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton)*