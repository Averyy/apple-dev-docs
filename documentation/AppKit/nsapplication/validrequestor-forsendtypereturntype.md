# validRequestor(forSendType:returnType:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the receiver can send and receive the specified pasteboard types.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?
```

#### Return Value

The object that can send and receive the specified types or `nil` if the receiver knows of no object that can send and receive data of that type.

#### Discussion

This message is sent to all responders in a responder chain. `NSApp` is typically the last item in the responder chain, so it usually receives this message only if none of the current responders can send `sendType` data and accept back `returnType` data.

The receiver passes this message on to its delegate if the delegate can respond (and isn’t an `NSResponder` object with its own next responder). If the delegate can’t respond or returns `nil`, this method returns `nil`. If the delegate can find an object that can send `sendType` data and accept back `returnType` data, it returns that object.

## Parameters

- `sendType`: The pasteboard type the app needs to send.
- `returnType`: The pasteboard type the app needs to receive.

## See Also

- [func readSelection(from: NSPasteboard) -> Bool](nsservicesmenurequestor/readselection(from:).md)
  Reads data from the pasteboard and uses it to replace the current selection.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsresponder/validrequestor(forsendtype:returntype:).md)
  Overridden by subclasses to determine what services are available.
- [func registerServicesMenuSendTypes([NSPasteboard.PasteboardType], returnTypes: [NSPasteboard.PasteboardType])](nsapplication/registerservicesmenusendtypes(_:returntypes:).md)
  Registers the pasteboard types the receiver can send and receive in response to service requests.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nsservicesmenurequestor/writeselection(to:types:).md)
  Writes the current selection to the pasteboard.
- [var servicesProvider: Any?](nsapplication/servicesprovider.md)
  The object that provides the services the current app advertises in the Services menu of other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/validrequestor(forsendtype:returntype:))*