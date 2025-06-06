# NSTouchBar.CustomizationIdentifier

**Framework**: AppKit  
**Kind**: typealias

The default type for a Touch Bar customization identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
typealias CustomizationIdentifier = String
```

## See Also

- [var customizationIdentifier: NSTouchBar.CustomizationIdentifier?](nstouchbar/customizationidentifier-swift.property.md)
  A globally unique string that makes the Touch Bar eligible for user customization.
- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationrequireditemidentifiers.md)
  An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.
- [class var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool](nstouchbar/isautomaticcustomizetouchbarmenuitemenabled.md)
  A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/customizationidentifier-swift.typealias)*