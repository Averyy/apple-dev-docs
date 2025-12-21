# tokenFieldCell(_:writeRepresentedObjects:to:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate the opportunity to write custom pasteboard types to the pasteboard for the represented objects in `objects`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, writeRepresentedObjects objects: [Any], to pboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the delegate writes the represented objects to the pasteboard, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. If [`false`](https://developer.apple.com/documentation/Swift/false), the token field writes the display strings to the [`NSStringPboardType`](nsstringpboardtype.md) pasteboard.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `objects`: An array of represented objects associated with the token field cell.
- `pboard`: The pasteboard to which to write the represented objects.

## See Also

- [func tokenFieldCell(NSTokenFieldCell, readFrom: NSPasteboard) -> [Any]?](nstokenfieldcelldelegate/tokenfieldcell(_:readfrom:).md)
  Allows the delegate to return an array of objects representing the data read from `pboard`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:writerepresentedobjects:to:))*