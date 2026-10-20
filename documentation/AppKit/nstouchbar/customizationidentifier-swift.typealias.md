# NSTouchBar.CustomizationIdentifier

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

The default type for a Touch Bar customization identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
typealias CustomizationIdentifier = String
```

```c
typedef NSString * NSTouchBarCustomizationIdentifier;
```

## See Also

### Configuring user customization
- [var customizationIdentifier: NSTouchBar.CustomizationIdentifier?](./customizationidentifier-swift.property.md)
  A globally unique string that makes the Touch Bar eligible for user customization.
- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](./customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier]](./customizationrequireditemidentifiers.md)
  An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.
- [class var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool](./isautomaticcustomizetouchbarmenuitemenabled.md)
  A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/customizationidentifier-swift.typealias)*