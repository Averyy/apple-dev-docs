# tokenFieldCell(_:writeRepresentedObjects:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate the opportunity to write custom pasteboard types to the pasteboard for the represented objects in `objects`.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, writeRepresentedObjects objects: [Any], to pboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell writeRepresentedObjects:(NSArray *) objects toPasteboard:(NSPasteboard *) pboard;
```

#### Return Value

[`true`](../../Swift/true.md) if the delegate writes the represented objects to the pasteboard, [`false`](../../Swift/false.md) otherwise. If [`false`](../../Swift/false.md), the token field writes the display strings to the [`NSStringPboardType`](../nsstringpboardtype.md) pasteboard.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `objects`: An array of represented objects associated with the token field cell.
- `pboard`: The pasteboard to which to write the represented objects.

## See Also

### Reading To and Writing From the Pasteboard
- [func tokenFieldCell(NSTokenFieldCell, readFrom: NSPasteboard) -> [Any]?](./tokenfieldcell%28_,readfrom%29.md)
  Allows the delegate to return an array of objects representing the data read from `pboard`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:writerepresentedobjects:to:))*