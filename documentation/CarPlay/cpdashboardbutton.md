# CPDashboardButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A shortcut button for placement on the CarPlay Dashboard.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class CPDashboardButton
```

```objc
@interface CPDashboardButton : NSObject
```

## Topics

### Creating a Dashboard Button
- [init(titleVariants: [String], subtitleVariants: [String], image: UIImage, handler: ((CPDashboardButton) -> Void)?)](./cpdashboardbutton/init%28titlevariants,subtitlevariants,image,handler%29.md)
  Creates a dashboard button that displays a title, an optional subtitle, and an image.
### Accessing the Button Configuration
- [var titleVariants: [String]](./cpdashboardbutton/titlevariants.md)
  The array of title variants for the button.
- [var subtitleVariants: [String]](./cpdashboardbutton/subtitlevariants.md)
  The array of subtitle variants for the button.
- [var image: UIImage](./cpdashboardbutton/image.md)
  The image the button displays.
### Initializers
- [init?(coder: NSCoder)](./cpdashboardbutton/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Providing Dashboard Buttons
- [var shortcutButtons: [CPDashboardButton]](./cpdashboardcontroller/shortcutbuttons.md)
  An array of shortcut buttons to display on the CarPlay Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton)*