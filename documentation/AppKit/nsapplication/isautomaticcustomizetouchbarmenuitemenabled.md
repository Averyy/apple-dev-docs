# isAutomaticCustomizeTouchBarMenuItemEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool { get set }
```

```objc
@property (getter=isAutomaticCustomizeTouchBarMenuItemEnabled) BOOL automaticCustomizeTouchBarMenuItemEnabled;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), AppKit adds a standard item to the app’s View menu that users can select to customize the Touch Bar contents, but only if a Touch Bar is present. If the View menu is unavailable, AppKit adds the item to either the Windows or App menu.

If you prefer to provide a customize menu item, set [`isAutomaticCustomizeTouchBarMenuItemEnabled`](./isautomaticcustomizetouchbarmenuitemenabled.md) to [`false`](../../Swift/false.md), and create the menu item with an action of [`toggleTouchBarCustomizationPalette(_:)`](./toggletouchbarcustomizationpalette%28_%29.md).

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Accessing the Main Menu
- [var mainMenu: NSMenu?](./mainmenu.md)
  The app’s main menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isautomaticcustomizetouchbarmenuitemenabled)*