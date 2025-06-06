# itemIdentifiers

**Framework**: AppKit  
**Kind**: property

The list of identifiers for the current items in the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var itemIdentifiers: [NSTouchBarItem.Identifier] { get }
```

#### Discussion

If the user has not customized the bar, this property’s value is the same as that of the [`defaultItemIdentifiers`](nstouchbar/defaultitemidentifiers.md) property.

The system  archive this property.

## See Also

- [var customizationIdentifier: NSTouchBar.CustomizationIdentifier?](nstouchbar/customizationidentifier-swift.property.md)
  A globally unique string that makes the Touch Bar eligible for user customization.
- [var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationrequireditemidentifiers.md)
  An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.
- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [var defaultItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/defaultitemidentifiers.md)
  A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.
- [var isVisible: Bool](nstouchbar/isvisible.md)
  A Boolean value that Indicates whether the Touch Bar is eligible for display.
- [func item(forIdentifier: NSTouchBarItem.Identifier) -> NSTouchBarItem?](nstouchbar/item(foridentifier:).md)
  Returns the Touch Bar item that corresponds to a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/itemidentifiers)*