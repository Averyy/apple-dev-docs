# CPGridButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A menu item button displayed on a grid template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPGridButton
```

```objc
@interface CPGridButton : NSObject
```

## Topics

### Creating a grid button
- [convenience init(titleVariants: [String], image: UIImage, handler: ((CPGridButton) -> Void)?)](./cpgridbutton/init%28titlevariants,image,handler%29.md)
  Creates a grid button with the specified title variants, image, and action handler.
- [init(titleVariants: [String], image: UIImage, messageConfiguration: CPMessageGridItemConfiguration?, handler: ((CPGridButton) -> Void)?)](./cpgridbutton/init%28titlevariants,image,messageconfiguration,handler%29.md)
  Initialize a button with a title, image, and message configuration.
- [init?(coder: NSCoder)](./cpgridbutton/init%28coder%29.md)
### Managing the button content
- [var image: UIImage](./cpgridbutton/image.md)
  The image displayed on the button.
- [func updateImage(UIImage)](./cpgridbutton/updateimage%28_%29.md)
- [var titleVariants: [String]](./cpgridbutton/titlevariants.md)
  An array of title variants for the button.
- [func updateTitleVariants([String])](./cpgridbutton/updatetitlevariants%28_%29.md)
### Enabling and disabling the button
- [var isEnabled: Bool](./cpgridbutton/isenabled.md)
  A Boolean value that enables and disables the grid button.
### Instance Properties
- [var messageConfiguration: CPMessageGridItemConfiguration?](./cpgridbutton/messageconfiguration.md)

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

### Grids
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPMessageGridItemConfiguration](./cpmessagegriditemconfiguration.md)
  A type that associates message-related information with a grid button.
- [let CPGridTemplateMaximumItems: Int](./cpgridtemplatemaximumitems.md)
  The maximum number of buttons that a grid template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton)*