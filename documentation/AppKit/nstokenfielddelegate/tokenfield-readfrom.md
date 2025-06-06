# tokenField(_:readFrom:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to return an array of objects representing the data read from the specified pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, readFrom pboard: NSPasteboard) -> [Any]?
```

#### Return Value

An array of represented objects created from the pasteboard data.

## Parameters

- `tokenField`: The token field that sent the message.
- `pboard`: The pasteboard from which to read the represented objects.

## See Also

- [func tokenField(NSTokenField, writeRepresentedObjects: [Any], to: NSPasteboard) -> Bool](nstokenfielddelegate/tokenfield(_:writerepresentedobjects:to:).md)
  Sent so the delegate can write represented objects to the pasteboard corresponding to a given array of display strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:readfrom:))*