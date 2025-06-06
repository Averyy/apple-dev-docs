# init(title:image:identifier:options:children:)

**Framework**: UIKit  
**Kind**: init

Creates a new menu with the specified values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String = "", image: UIImage? = nil, identifier: UIMenu.Identifier? = nil, options: UIMenu.Options = [], children: [UIMenuElement] = [])
```

## Parameters

- `title`: The title of the menu.
- `image`: The image to display next to the menu’s title.
- `identifier`: The unique identifier for the menu. When creating standard menus for your app, specify an appropriate constant defined in  . For custom menus, specify a custom reverse domain name value, or specify   to let this method create a unique identifier for you.
- `options`: Additional configuration options for the menu. For a list of possible values, see  .
- `children`: The menu elements in the menu. Specify leaf menu elements using   subclasses like  ,  , or  , and specify submenus using   objects. You may specify an empty array if the menu has no child menu elements.

## See Also

- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIMenu.Identifier?, options: UIMenu.Options, preferredElementSize: UIMenu.ElementSize, children: [UIMenuElement])](uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:).md)
  Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [UIMenu.Identifier](uimenu/identifier-swift.struct.md)
  Constants you use to identify an app’s standard menus.
- [UIMenu.Options](uimenu/options-swift.struct.md)
  Options you use to configure a menu’s appearance.
- [init?(coder: NSCoder)](uimenu/init(coder:).md)
  Creates a menu from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/init(title:image:identifier:options:children:))*