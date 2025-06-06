# escapeKeyReplacementItemIdentifier

**Framework**: AppKit  
**Kind**: property

The identifier of an item that replaces the system-provided button in the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var escapeKeyReplacementItemIdentifier: NSTouchBarItem.Identifier? { get set }
```

#### Discussion

To replace the system-provided button, set [`escapeKeyReplacementItemIdentifier`](nstouchbar/escapekeyreplacementitemidentifier.md) to the identifier of an [`NSTouchBarItem`](nstouchbaritem.md) instance. You must also include the item instance in the Touch Bar’s [`templateItems`](nstouchbar/templateitems.md) array, or return the item when the Touch Bar calls the [`touchBar(_:makeItemForIdentifier:)`](nstouchbardelegate/touchbar(_:makeitemforidentifier:).md) delegate method.

Devices that include the Touch Bar (second generation) have a dedicated Escape key located to the left of the Touch Bar. By default, the Touch Bar hides the system-provided button and its replacement on these devices. However, if you set the replacement item’s [`visibilityPriority`](nstouchbaritem/visibilitypriority.md) to [`high`](nstouchbaritem/priority/high.md), the Touch Bar shows the item and reduces the visible space of the app region.

## See Also

- [var delegate: (any NSTouchBarDelegate)?](nstouchbar/delegate.md)
  The delegate that provides items to the Touch Bar.
- [var templateItems: Set<NSTouchBarItem>](nstouchbar/templateitems.md)
  The primary source of items that the Touch Bar uses to fill its private items array, unless you provide items using a delegate.
- [var defaultItemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/defaultitemidentifiers.md)
  A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.
- [var principalItemIdentifier: NSTouchBarItem.Identifier?](nstouchbar/principalitemidentifier.md)
  The identifier of an item you want the system to center in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/escapekeyreplacementitemidentifier)*