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

- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [Pasteboard Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)
- [Services Implementation Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html#//apple_ref/doc/uid/10000101i)
- [func pasteboardFinishedWithDataProvider(NSPasteboard)](nspasteboarditemdataprovider/pasteboardfinishedwithdataprovider(_:).md)
  Informs the receiver that the pasteboard no longer needs the data provider for any of its pasteboard items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider/pasteboard(_:item:providedatafortype:))*