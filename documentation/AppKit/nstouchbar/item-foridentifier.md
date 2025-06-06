# item(forIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns the Touch Bar item that corresponds to a given identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func item(forIdentifier identifier: NSTouchBarItem.Identifier) -> NSTouchBarItem?
```

#### Return Value

A Touch Bar item if one exists for the given identifier; otherwise, returns `nil`.

#### Discussion

The system returns items (instances of the [`NSTouchBarItem`](nstouchbaritem.md) class) as it finds them, according to the following search order, listed here from first-searched to last-searched:

1. Items in the bar’s private array, which are reflected in the value of the [`itemIdentifiers`](nstouchbar/itemidentifiers.md) array.
2. Items in the [`templateItems`](nstouchbar/templateitems.md) array.
3. Items returned from the bar delegate’s [`touchBar(_:makeItemForIdentifier:)`](nstouchbardelegate/touchbar(_:makeitemforidentifier:).md) method.

Your app never needs to instantiate spacing or proxy items because these are created by the system directly, according to their identifiers, as shown in the table below.

| Constant | Resulting item |
| --- | --- |
| [`fixedSpaceSmall`](nstouchbaritem/identifier-swift.struct/fixedspacesmall.md) | small space |
| [`fixedSpaceLarge`](nstouchbaritem/identifier-swift.struct/fixedspacelarge.md) | large space |
| [`flexibleSpace`](nstouchbaritem/identifier-swift.struct/flexiblespace.md) | flexible space |
| [`otherItemsProxy`](nstouchbaritem/identifier-swift.struct/otheritemsproxy.md) | proxy placeholder |

For more on the proxy placeholder, see [`Composition and nesting`](nstouchbar#Composition-and-nesting.md).

## See Also

- [var isVisible: Bool](nstouchbar/isvisible.md)
  A Boolean value that Indicates whether the Touch Bar is eligible for display.
- [var itemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/itemidentifiers.md)
  The list of identifiers for the current items in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/item(foridentifier:))*