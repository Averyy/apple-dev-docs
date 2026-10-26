# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a menu from data in an unarchiver.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

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
- [UIMenu.Options](./options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [+ menuWithChildren:](./menuwithchildren_.md)
  Creates a new menu with the specified child elements.
- [+ menuWithTitle:children:](./menuwithtitle_children_.md)
  Creates a menu with the specified title and child menu elements.
- [+ menuWithTitle:image:identifier:options:children:](./menuwithtitle_image_identifier_options_children_.md)
  Creates a new menu with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/init(coder:))*