# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate that provides items to the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
weak var delegate: (any NSTouchBarDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTouchBarDelegate> delegate;
```

#### Discussion

Employ a bar delegate, according to the needs of your app, to dynamically create items ([`NSTouchBarItem`](../nstouchbaritem.md) instances). For more information, see [Item objects](../nstouchbar.md#Item-objects).

This property is conditionally archived, as described in the [`encodeConditionalObject(_:forKey:)`](../../Foundation/nskeyedarchiver/encodeconditionalobject%28_,forkey%29.md) method.

## See Also

### Providing bar items
- [var templateItems: Set<NSTouchBarItem>](./templateitems.md)
  The primary source of items that the Touch Bar uses to fill its private items array, unless you provide items using a delegate.
- [var defaultItemIdentifiers: [NSTouchBarItem.Identifier]](./defaultitemidentifiers.md)
  A required list of identifiers for items that you want to appear in the Touch Bar after instantiating it.
- [var principalItemIdentifier: NSTouchBarItem.Identifier?](./principalitemidentifier.md)
  The identifier of an item you want the system to center in the Touch Bar.
- [var escapeKeyReplacementItemIdentifier: NSTouchBarItem.Identifier?](./escapekeyreplacementitemidentifier.md)
  The identifier of an item that replaces the system-provided button in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/delegate)*