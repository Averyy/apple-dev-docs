# NSMenuItemBadge

**Framework**: AppKit  
**Kind**: class

A control that provides additional quantitative information specific to a menu item, such as the number of available updates.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class NSMenuItemBadge
```

#### Overview

You create a badge using an initializer or a predefined factory method, and then you assign it to the [`badge`](nsmenuitem/badge.md) property of a [`NSMenuItem`](nsmenuitem.md) for display.

![A menu containing five menu items with each menu item displaying a different style of badge. A NSMenuItem callout points to a menu item in the menu. A NSMenuItemBadge call out points to the badge that displays to the right of the menu item.](https://docs-assets.developer.apple.com/published/23a4abb17eb26672bddbe46fb5b592dd/media-4304515%402x.png)

For example, to display a badge with a count, use the [`init(count:)`](nsmenuitembadge/init(count:).md) initalizer, passing in the value of `count` as an `Int`.

To display a badge with a custom string, use the [`init(string:)`](nsmenuitembadge/init(string:).md) initializer, passing in the string you want to display.

To display a badge using a predefined [`NSMenuItemBadge.BadgeType`](nsmenuitembadge/badgetype.md), use a factory method such as [`newItems(count:)`](nsmenuitembadge/newitems(count:).md), passing in the `count` of the badge to display.

> ❗ **Important**:  If you use one of the predefined badge types, the system localizes and pluralizes the string for you. If you create your own custom badge string, you need to localize and pluralize that string yourself. For more information on how to localize and pluralize text, see [`Localizing and varying text with a string catalog`](https://developer.apple.com/documentation/Xcode/localizing-and-varying-text-with-a-string-catalog).

 If you use one of the predefined badge types, the system localizes and pluralizes the string for you. If you create your own custom badge string, you need to localize and pluralize that string yourself. For more information on how to localize and pluralize text, see [`Localizing and varying text with a string catalog`](https://developer.apple.com/documentation/Xcode/localizing-and-varying-text-with-a-string-catalog).

The default value of this property is `nil`.

## Topics

### Creating menu item badges
- [init(count: Int)](nsmenuitembadge/init(count:).md)
  Creates a badge with a count and an empty string.
- [init(string: String)](nsmenuitembadge/init(string:).md)
  Creates a badge with the provided custom string.
### Creating badges of a specific type
- [class func alerts(count: Int) -> Self](nsmenuitembadge/alerts(count:).md)
  Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.
- [class func newItems(count: Int) -> Self](nsmenuitembadge/newitems(count:).md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [class func updates(count: Int) -> Self](nsmenuitembadge/updates(count:).md)
  Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.
- [NSMenuItemBadge.BadgeType](nsmenuitembadge/badgetype.md)
  Constants that define types of badges for display.
### Accessing menu item badge attributes
- [var itemCount: Int](nsmenuitembadge/itemcount.md)
  The number of items the badge displays.
- [var stringValue: String?](nsmenuitembadge/stringvalue-fc9f.md)
  The string representation of the badge when it displays.
- [var type: NSMenuItemBadge.BadgeType](nsmenuitembadge/type.md)
  The type of items the badge displays.
### Instance Properties
- [var stringValue: String?](nsmenuitembadge/stringvalue-32sbt.md)
  The string representation of the badge as it would appear when the badge is displayed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSMenu](nsmenu.md)
  An object that manages an app’s menus.
- [class NSMenuItem](nsmenuitem.md)
  A command item in an app menu.
- [protocol NSMenuDelegate](nsmenudelegate.md)
  The optional methods implemented by delegates of [`NSMenu`](nsmenu.md) objects to manage menu display and handle some events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge)*