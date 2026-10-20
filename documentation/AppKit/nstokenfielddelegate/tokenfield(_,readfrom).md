# tokenField(_:readFrom:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to return an array of objects representing the data read from the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, readFrom pboard: NSPasteboard) -> [Any]?
```

```objc
- (NSArray *) tokenField:(NSTokenField *) tokenField readFromPasteboard:(NSPasteboard *) pboard;
```

#### Return Value

An array of represented objects created from the pasteboard data.

## Parameters

- `tokenField`: The token field that sent the message.
- `pboard`: The pasteboard from which to read the represented objects.

## See Also

### Reading To and Writing From the Pasteboard
- [func tokenField(NSTokenField, writeRepresentedObjects: [Any], to: NSPasteboard) -> Bool](./tokenfield%28_,writerepresentedobjects,to%29.md)
  Sent so the delegate can write represented objects to the pasteboard corresponding to a given array of display strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:readfrom:))*