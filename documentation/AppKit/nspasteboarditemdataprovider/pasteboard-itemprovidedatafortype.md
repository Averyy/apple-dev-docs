# pasteboard(_:item:provideDataForType:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the receiver to provide data for a specified type to a given pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
nonisolated
func pasteboard(_ pasteboard: NSPasteboard?, item: NSPasteboardItem, provideDataForType type: NSPasteboard.PasteboardType)
```

#### Discussion

The receiver was previously set as the provider using [`setDataProvider(_:forTypes:)`](nspasteboarditem/setdataprovider(_:fortypes:).md).

## Parameters

- `pasteboard`: A pasteboard to which the receiver has promised to provide data.
- `item`: A pasteboard item for which the receiver has promised to provide data
- `type`: A UTI type string.

## See Also

- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.
- [func pasteboardFinishedWithDataProvider(NSPasteboard)](nspasteboarditemdataprovider/pasteboardfinishedwithdataprovider(_:).md)
  Informs the receiver that the pasteboard no longer needs the data provider for any of its pasteboard items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider/pasteboard(_:item:providedatafortype:))*