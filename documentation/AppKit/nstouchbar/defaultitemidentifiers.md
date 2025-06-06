# defaultItemIdentifiers

**Framework**: AppKit  
**Kind**: property

A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var defaultItemIdentifiers: [NSTouchBarItem.Identifier] { get set }
```

#### Discussion

Always specify this property for an [`NSTouchBar`](nstouchbar.md) object, even if you elect to make the bar noncustomizable. The system:

- Shows this list’s items by default when the system displays the bar.
- Includes a preconfigured bar, containing these items, in the associated customization UI (when you have assigned the bar a [`customizationIdentifier`](nstouchbar/customizationidentifier-swift.property.md) property value); the user can drag the default bar into the Touch Bar, should they want to return to the default configuration.

The system archives this property.

## See Also

- [var customizationIdentifier: NSTouchBar.CustomizationIdentifier?](nstouchbar/customizationidentifier-swift.property.md)
  A globally unique string that makes the Touch Bar eligible for user customization.
- [var customizationRequiredItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationrequireditemidentifiers.md)
  An optional list of identifiers for items you want to always appear in the Touch Bar and which the user can’t remove during customization.
- [var customizationAllowedItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/customizationalloweditemidentifiers.md)
  A list of identifiers for items to show in the Touch Bar’s customization UI.
- [var itemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/itemidentifiers.md)
  The list of identifiers for the current items in the Touch Bar.
- [var delegate: (any NSTouchBarDelegate)?](nstouchbar/delegate.md)
  The delegate that provides items to the Touch Bar.
- [var templateItems: Set<NSTouchBarItem>](nstouchbar/templateitems.md)
  The primary source of items that the Touch Bar uses to fill its private items array, unless you provide items using a delegate.
- [var principalItemIdentifier: NSTouchBarItem.Identifier?](nstouchbar/principalitemidentifier.md)
  The identifier of an item you want the system to center in the Touch Bar.
- [var escapeKeyReplacementItemIdentifier: NSTouchBarItem.Identifier?](nstouchbar/escapekeyreplacementitemidentifier.md)
  The identifier of an item that replaces the system-provided button in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/defaultitemidentifiers)*