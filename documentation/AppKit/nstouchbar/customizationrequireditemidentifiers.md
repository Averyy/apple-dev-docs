# customizationRequiredItemIdentifiers

**Framework**: AppKit  
**Kind**: property

An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier] { get set }
```

#### Discussion

Configure this property at your discretion, depending on the design of your app.

The system archives this property.

## See Also

- [var defaultItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/defaultitemidentifiers.md)
  A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.
- [var itemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/itemidentifiers.md)
  The list of identifiers for the current items in the Touch Bar.
- [var customizationIdentifier: NSTouchBar.CustomizationIdentifier?](nstouchbar/customizationidentifier-swift.property.md)
  A globally unique string that makes the Touch Bar eligible for user customization.
- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [NSTouchBar.CustomizationIdentifier](nstouchbar/customizationidentifier-swift.typealias.md)
  The default type for a Touch Bar customization identifier.
- [class var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool](nstouchbar/isautomaticcustomizetouchbarmenuitemenabled.md)
  A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/customizationrequireditemidentifiers)*