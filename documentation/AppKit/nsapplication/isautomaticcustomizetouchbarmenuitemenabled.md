# isAutomaticCustomizeTouchBarMenuItemEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), AppKit adds a standard item to the app’s View menu that users can select to customize the Touch Bar contents, but only if a Touch Bar is present. If the View menu is unavailable, AppKit adds the item to either the Windows or App menu.

If you prefer to provide a customize menu item, set [`isAutomaticCustomizeTouchBarMenuItemEnabled`](nsapplication/isautomaticcustomizetouchbarmenuitemenabled.md) to [`false`](https://developer.apple.com/documentation/Swift/false), and create the menu item with an action of [`toggleTouchBarCustomizationPalette(_:)`](nsapplication/toggletouchbarcustomizationpalette(_:).md).

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var mainMenu: NSMenu?](nsapplication/mainmenu.md)
  The app’s main menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isautomaticcustomizetouchbarmenuitemenabled)*