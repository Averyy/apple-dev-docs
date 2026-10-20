# tokenFieldCell(_:readFrom:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to return an array of objects representing the data read from `pboard`.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, readFrom pboard: NSPasteboard) -> [Any]?
```

```objc
- (NSArray *) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell readFromPasteboard:(NSPasteboard *) pboard;
```

#### Return Value

An array of represented objects created from the pasteboard data.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `pboard`: The pasteboard from which to read the represented objects.

## See Also

### Reading To and Writing From the Pasteboard
- [func tokenFieldCell(NSTokenFieldCell, writeRepresentedObjects: [Any], to: NSPasteboard) -> Bool](./tokenfieldcell%28_,writerepresentedobjects,to%29.md)
  Allows the delegate the opportunity to write custom pasteboard types to the pasteboard for the represented objects in `objects`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:readfrom:))*