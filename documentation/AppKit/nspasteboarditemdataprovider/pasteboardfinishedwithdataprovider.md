# pasteboardFinishedWithDataProvider(_:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the pasteboard no longer needs the data provider for any of its pasteboard items.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
optional func pasteboardFinishedWithDataProvider(_ pasteboard: NSPasteboard)
```

#### Discussion

One data provider can provide data for more than one pasteboard item. This method is called when the pasteboard no longer needs the data provider for any of its pasteboard items. This can be either because the data provider has fulfilled all promises, or because ownership of the pasteboard has changed.

## Parameters

- `pasteboard`: A pasteboard.

## See Also

- [func pasteboard(NSPasteboard?, item: NSPasteboardItem, provideDataForType: NSPasteboard.PasteboardType)](nspasteboarditemdataprovider/pasteboard(_:item:providedatafortype:).md)
  Asks the receiver to provide data for a specified type to a given pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider/pasteboardfinishedwithdataprovider(_:))*