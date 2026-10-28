# system

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The menu system that the menu builder modifies.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var system: UIMenuSystem { get }
```

```objc
@property (nonatomic, readonly) UIMenuSystem * system;
```

## Discussion

Always check the [`system`](./system.md) property to determine which menu system the builder is modifying before you add and remove menus. For example, when you want to modify the main menu bar, check [`system`](./system.md) for [`main`](../uimenusystem/main.md).

```swift
override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)
    
    // Ensure that the builder is modifying the menu bar system.
    guard builder.system == UIMenuSystem.main else { return }
    
    let refreshCommand = UICommand(title: "Refresh", action: #selector(refreshData(_:)))
    let refreshMenu = UIMenu(title: "", options: .displayInline, children: [refreshCommand])

    // Insert the menu into the File menu before the Close menu.
    builder.insertSibling(refreshMenu, beforeMenu: .close)
}
```

## See Also

### Getting menu systems and elements
- [func menu(for: UIMenu.Identifier) -> UIMenu?](./menu%28for%29.md)
  Gets the menu for the specified menu identifier.
- [func action(for: UIAction.Identifier) -> UIAction?](./action%28for%29.md)
  Gets the action for the specified action identifier.
- [func command(for: Selector, propertyList: Any?) -> UICommand?](./command%28for,propertylist%29.md)
  Gets the command for the specified selector and property list.
- [- commandForAction:propertyList:](./commandforaction_propertylist_.md)
  Gets the command for the specified selector and property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/system)*