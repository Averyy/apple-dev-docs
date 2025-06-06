# menuItems

**Framework**: UIKit  
**Kind**: property

The custom menu items for the editing menu.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var menuItems: [UIMenuItem]? { get set }
```

#### Discussion

The default value is `nil` (no custom menu items). Each menu item is an instance of the UIMenuItem class. You may create your own menu items, each with its own title and action selector, and add them to the editing menu through this property. Custom items appear in the menu after any system menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/menuitems)*