# init(coder:)

**Framework**: UIKit  
**Kind**: init

Creates a menu from data in an unarchiver.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

## See Also

- [convenience init(title: String, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:image:identifier:options:children:).md)
  Creates a new menu with the specified values.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Identifier](uimenu/identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [UIMenu.Options](uimenu/options-swift.struct.md)
  Options you use to configure a menu’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/init(coder:))*