# menu

**Framework**: AppKit  
**Kind**: property

The menu that contains the button’s alternate actions.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var menu: NSMenu { get set }
```

#### Discussion

The combo button executes the menu item’s action when someone selects that item, so make sure to configure the targets and actions for each menu item in your menu.

An [`NSComboButton`](nscombobutton.md) doesn’t support the addition of a contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/menu)*