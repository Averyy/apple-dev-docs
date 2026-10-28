# validRequestor(forSendType:returnType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the receiver can send and receive the specified pasteboard types.

**Availability**:
- macOS

## Declaration

```swift
func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?
```

```objc
- (id) validRequestorForSendType:(NSPasteboardType) sendType returnType:(NSPasteboardType) returnType;
```

## Return Value

The object that can send and receive the specified types or `nil` if the receiver knows of no object that can send and receive data of that type.

## Discussion

This message is sent to all responders in a responder chain. `NSApp` is typically the last item in the responder chain, so it usually receives this message only if none of the current responders can send `sendType` data and accept back `returnType` data.

The receiver passes this message on to its delegate if the delegate can respond (and isn’t an `NSResponder` object with its own next responder). If the delegate can’t respond or returns `nil`, this method returns `nil`. If the delegate can find an object that can send `sendType` data and accept back `returnType` data, it returns that object.

## Parameters

- `sendType`: The pasteboard type the app needs to send.
- `returnType`: The pasteboard type the app needs to receive.

## See Also

### Related Documentation
- [func readSelection(from: NSPasteboard) -> Bool](../nsservicesmenurequestor/readselection%28from%29.md)
  Reads data from the pasteboard and uses it to replace the current selection.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](../nsresponder/validrequestor%28forsendtype,returntype%29.md)
  Overridden by subclasses to determine what services are available.
- [func registerServicesMenuSendTypes([NSPasteboard.PasteboardType], returnTypes: [NSPasteboard.PasteboardType])](./registerservicesmenusendtypes%28_,returntypes%29.md)
  Registers the pasteboard types the receiver can send and receive in response to service requests.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](../nsservicesmenurequestor/writeselection%28to,types%29.md)
  Writes the current selection to the pasteboard.
### Providing services
- [var servicesProvider: Any?](./servicesprovider.md)
  The object that provides the services the current app advertises in the Services menu of other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/validrequestor(forsendtype:returntype:))*