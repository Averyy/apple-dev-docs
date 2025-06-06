# init(pasteboardPropertyList:ofType:)

**Framework**: AppKit  
**Kind**: init  
**Required**: Yes

Initializes an instance with a property list object and a type string.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(pasteboardPropertyList propertyList: Any, ofType type: NSPasteboard.PasteboardType)
```

#### Return Value

An object initialized using the data in `propertyList`.

#### Discussion

This method is considered optional because, if [`readableTypes(for:)`](nspasteboardreading/readabletypes(for:).md) returns just a single type, and that type uses the [`asKeyedArchive`](nspasteboard/readingoptions/askeyedarchive.md) reading option, then instances are initialized using [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) instead of this method.

## Parameters

- `propertyList`: By default, the property list object is an instance of  . If you implement   and specify an option other than  , the   may be any other property list object.
- `type`: A UTI supported by the receiver for reading (one of the types returned by  ).

## See Also

- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [Pasteboard Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)
- [Services Implementation Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html#//apple_ref/doc/uid/10000101i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardreading/init(pasteboardpropertylist:oftype:))*