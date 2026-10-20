# isAutomaticCustomizeTouchBarMenuItemEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
class var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool { get set }
```

```objc
@property (class, getter=isAutomaticCustomizeTouchBarMenuItemEnabled) BOOL automaticCustomizeTouchBarMenuItemEnabled;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), AppKit adds a standard item to the app’s View menu that users can select to customize the Touch Bar contents, but only if a Touch Bar is present. If the View menu is unavailable, AppKit adds the item to either the Windows or App menu.

If you prefer to provide a customize menu item, set [`isAutomaticCustomizeTouchBarMenuItemEnabled`](./isautomaticcustomizetouchbarmenuitemenabled.md) to [`false`](../../Swift/false.md), and create the menu item with an action of [`toggleTouchBarCustomizationPalette(_:)`](../nsapplication/toggletouchbarcustomizationpalette%28_%29.md).

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring user customization
- [var customizationIdentifier: NSTouchBar.CustomizationIdentifier?](./customizationidentifier-swift.property.md)
  A globally unique string that makes the Touch Bar eligible for user customization.
- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](./customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier]](./customizationrequireditemidentifiers.md)
  An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.
- [NSTouchBar.CustomizationIdentifier](./customizationidentifier-swift.typealias.md)
  The default type for a Touch Bar customization identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/isautomaticcustomizetouchbarmenuitemenabled)*