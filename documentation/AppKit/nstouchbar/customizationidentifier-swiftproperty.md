# customizationIdentifier

**Framework**: AppKit  
**Kind**: property

A globally unique string that makes the Touch Bar eligible for user customization.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var customizationIdentifier: NSTouchBar.CustomizationIdentifier? { get set }
```

#### Discussion

To make an [`NSTouchBar`](nstouchbar.md) object eligible for user customization, assign it a globally unique [`customizationIdentifier`](nstouchbar/customizationidentifier-swift.property.md) identifier. For the identifier string, use reverse-DNS style, such as “`com.company-name.app-name.alphanumeric-ID`”.

The system archives this property.

## See Also

- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationrequireditemidentifiers.md)
  An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.
- [NSTouchBar.CustomizationIdentifier](nstouchbar/customizationidentifier-swift.typealias.md)
  The default type for a Touch Bar customization identifier.
- [class var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool](nstouchbar/isautomaticcustomizetouchbarmenuitemenabled.md)
  A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/customizationidentifier-swift.property)*