# validRequestor(forSendType:returnType:)

**Framework**: AppKit  
**Kind**: method

Searches for an object that responds to a Services request.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?
```

#### Return Value

The object that responds to the services request; `nil` when none is found.

#### Discussion

Messages to perform this method are initiated by the Services menu. It’s part of the mechanism that passes [`validRequestor(forSendType:returnType:)`](nswindow/validrequestor(forsendtype:returntype:).md) messages up the responder chain.

This method works by forwarding the message to the window’s delegate if it responds (and provided it isn’t an `NSResponder` object with its own next responder). If the delegate doesn’t respond to the message or returns `nil` when sent it, this method forwards the message to the `NSApplication` object. If the `NSApplication` object returns `nil`, this method also returns `nil`. Otherwise this method returns the object returned by the delegate or the `NSApplication` object.

## Parameters

- `sendType`: The input type of the Services request.
- `returnType`: The return type of the Services request.

## See Also

- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsresponder/validrequestor(forsendtype:returntype:).md)
  Overridden by subclasses to determine what services are available.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsapplication/validrequestor(forsendtype:returntype:).md)
  Indicates whether the receiver can send and receive the specified pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/validrequestor(forsendtype:returntype:))*