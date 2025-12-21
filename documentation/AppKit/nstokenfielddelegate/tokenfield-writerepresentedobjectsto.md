# tokenField(_:writeRepresentedObjects:to:)

**Framework**: AppKit  
**Kind**: method

Sent so the delegate can write represented objects to the pasteboard corresponding to a given array of display strings.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, writeRepresentedObjects objects: [Any], to pboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the delegate writes the represented objects to the pasteboard, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. If [`false`](https://developer.apple.com/documentation/Swift/false), the token field writes the display strings to the [`NSStringPboardType`](nsstringpboardtype.md) pasteboard.

## Parameters

- `tokenField`: The token field that sent the message.
- `objects`: An array of represented objects associated with the token field.
- `pboard`: The pasteboard to which to write the represented objects.

## See Also

- [func tokenField(NSTokenField, readFrom: NSPasteboard) -> [Any]?](nstokenfielddelegate/tokenfield(_:readfrom:).md)
  Allows the delegate to return an array of objects representing the data read from the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:writerepresentedobjects:to:))*