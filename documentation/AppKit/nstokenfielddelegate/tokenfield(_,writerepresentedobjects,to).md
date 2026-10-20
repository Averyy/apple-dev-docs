# tokenField(_:writeRepresentedObjects:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent so the delegate can write represented objects to the pasteboard corresponding to a given array of display strings.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, writeRepresentedObjects objects: [Any], to pboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) tokenField:(NSTokenField *) tokenField writeRepresentedObjects:(NSArray *) objects toPasteboard:(NSPasteboard *) pboard;
```

#### Return Value

[`true`](../../Swift/true.md) if the delegate writes the represented objects to the pasteboard, [`false`](../../Swift/false.md) otherwise. If [`false`](../../Swift/false.md), the token field writes the display strings to the [`NSStringPboardType`](../nsstringpboardtype.md) pasteboard.

## Parameters

- `tokenField`: The token field that sent the message.
- `objects`: An array of represented objects associated with the token field.
- `pboard`: The pasteboard to which to write the represented objects.

## See Also

### Reading To and Writing From the Pasteboard
- [func tokenField(NSTokenField, readFrom: NSPasteboard) -> [Any]?](./tokenfield%28_,readfrom%29.md)
  Allows the delegate to return an array of objects representing the data read from the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:writerepresentedobjects:to:))*