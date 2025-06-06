# principalItemIdentifier

**Framework**: AppKit  
**Kind**: property

The identifier of an item you want the system to center in the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var principalItemIdentifier: NSTouchBarItem.Identifier? { get set }
```

#### Discussion

The system attempts to center a principal item within the Touch Bar. If you want a group of items to appear centered in the Touch Bar, designate the group item (of type [`NSGroupTouchBarItem`](nsgrouptouchbaritem.md)) as the principal item.

If more than one bar in the responder chain is eligible to be visible in the Touch Bar, and more than one of those has a principal item, the system determines which one to center in the Touch Bar.

The system archives this property.

## See Also

- [var delegate: (any NSTouchBarDelegate)?](nstouchbar/delegate.md)
  The delegate that provides items to the Touch Bar.
- [var templateItems: Set<NSTouchBarItem>](nstouchbar/templateitems.md)
  The primary source of items that the Touch Bar uses to fill its private items array, unless you provide items using a delegate.
- [var defaultItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/defaultitemidentifiers.md)
  A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.
- [var escapeKeyReplacementItemIdentifier: NSTouchBarItem.Identifier?](nstouchbar/escapekeyreplacementitemidentifier.md)
  The identifier of an item that replaces the system-provided button in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/principalitemidentifier)*