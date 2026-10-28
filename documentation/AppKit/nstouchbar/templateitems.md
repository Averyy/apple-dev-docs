# templateItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The primary source of items that the Touch Bar uses to fill its private items array, unless you provide items using a delegate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var templateItems: Set<NSTouchBarItem> { get set }
```

```objc
@property (copy) NSSet<NSTouchBarItem *> * templateItems;
```

## Discussion

When a bar needs to fill its private items array with items ([`NSTouchBarItem`](../nstouchbaritem.md) instances), it employs a variety of potential sources. The first place it looks is this property. For more information, see [Item objects](../nstouchbar.md#Item-objects).

The system archives this property.

## See Also

### Providing bar items
- [var delegate: (any NSTouchBarDelegate)?](./delegate.md)
  The delegate that provides items to the Touch Bar.
- [var defaultItemIdentifiers: [NSTouchBarItem.Identifier]](./defaultitemidentifiers.md)
  A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.
- [var principalItemIdentifier: NSTouchBarItem.Identifier?](./principalitemidentifier.md)
  The identifier of an item you want the system to center in the Touch Bar.
- [var escapeKeyReplacementItemIdentifier: NSTouchBarItem.Identifier?](./escapekeyreplacementitemidentifier.md)
  The identifier of an item that replaces the system-provided button in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/templateitems)*