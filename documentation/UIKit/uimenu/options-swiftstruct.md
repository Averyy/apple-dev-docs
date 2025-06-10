# UIMenu.Options

**Framework**: UIKit  
**Kind**: struct

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

## Topics

### Options
- [static var displayInline: UIMenu.Options](uimenu/options-swift.struct/displayinline.md)
  An option indicating the menu displays inline with its parent menu instead of displaying as a submenu.
- [static var destructive: UIMenu.Options](uimenu/options-swift.struct/destructive.md)
  An option indicating the menu’s appearance represents a destructive action.
- [static var singleSelection: UIMenu.Options](uimenu/options-swift.struct/singleselection.md)
  An option indicating whether the menu and its submenus allow a single menu item that’s in the “on” state.
- [static var displayAsPalette: UIMenu.Options](uimenu/options-swift.struct/displayaspalette.md)
  An option indicating the menu displays as a row of menu elements for choosing from a collection of items.
### Initializers
- [init(rawValue: UInt)](uimenu/options-swift.struct/init(rawvalue:).md)
  Creates a menu options structure from data in an unarchiver.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [convenience init(title: String, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:image:identifier:options:children:).md)
  Creates a new menu with the specified values.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Identifier](uimenu/identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [init?(coder: NSCoder)](uimenu/init(coder:).md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct)*