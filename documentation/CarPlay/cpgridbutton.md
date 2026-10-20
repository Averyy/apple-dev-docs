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

### Creating a Grid Button
- [convenience init(titleVariants: [String], image: UIImage, handler: ((CPGridButton) -> Void)?)](./cpgridbutton/init%28titlevariants,image,handler%29.md)
  Creates a grid button with the specified title variants, image, and action handler.
### Controlling the Grid Button
- [var isEnabled: Bool](./cpgridbutton/isenabled.md)
  A Boolean value that enables and disables the grid button.
### Obtaining Grid Button Information
- [var titleVariants: [String]](./cpgridbutton/titlevariants.md)
  An array of title variants for the button.
- [var image: UIImage](./cpgridbutton/image.md)
  The image displayed on the button.
### Initializers
- [init?(coder: NSCoder)](./cpgridbutton/init%28coder%29.md)
- [init(titleVariants: [String], image: UIImage, messageConfiguration: CPMessageGridItemConfiguration?, handler: ((CPGridButton) -> Void)?)](./cpgridbutton/init%28titlevariants,image,messageconfiguration,handler%29.md)
  Initialize a button with a title, image, and message configuration.
### Instance Properties
- [var messageConfiguration: CPMessageGridItemConfiguration?](./cpgridbutton/messageconfiguration.md)
### Instance Methods
- [func updateImage(UIImage)](./cpgridbutton/updateimage%28_%29.md)
- [func updateTitleVariants([String])](./cpgridbutton/updatetitlevariants%28_%29.md)

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

### Creating a Grid Template
- [init(title: String?, gridButtons: [CPGridButton])](./cpgridtemplate/init%28title,gridbuttons%29.md)
  Creates a grid template with a title and a set of buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton)*