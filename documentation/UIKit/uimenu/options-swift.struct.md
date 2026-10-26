# UIMenu.Options

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Options you use to configure a menu’s appearance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Options
```

```c
enum UIMenuOptions : NSUInteger;
```

## Topics

### Options
- [static var displayInline: UIMenu.Options](./options-swift.struct/displayinline.md)
  An option indicating the menu displays inline with its parent menu instead of displaying as a submenu.
- [static var destructive: UIMenu.Options](./options-swift.struct/destructive.md)
  An option indicating the menu’s appearance represents a destructive action.
- [static var singleSelection: UIMenu.Options](./options-swift.struct/singleselection.md)
  An option indicating whether the menu and its submenus allow a single menu item that’s in the “on” state.
- [static var displayAsPalette: UIMenu.Options](./options-swift.struct/displayaspalette.md)
  An option indicating the menu displays as a row of menu elements for choosing from a collection of items.
### Initializers
- [init(rawValue: UInt)](./options-swift.struct/init%28rawvalue%29.md)
  Creates a menu options structure from data in an unarchiver.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a menu object
- [convenience init(title: String, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](./init%28title,image,identifier,options,children%29.md)
  Creates a new menu with the specified values.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](./init%28title,subtitle,image,identifier,options,children%29.md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](./init%28title,subtitle,image,identifier,options,preferredelementsize,children%29.md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Identifier](./identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a menu from data in an unarchiver.
- [+ menuWithChildren:](./menuwithchildren_.md)
  Creates a new menu with the specified child elements.
- [+ menuWithTitle:children:](./menuwithtitle_children_.md)
  Creates a menu with the specified title and child menu elements.
- [+ menuWithTitle:image:identifier:options:children:](./menuwithtitle_image_identifier_options_children_.md)
  Creates a new menu with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct)*