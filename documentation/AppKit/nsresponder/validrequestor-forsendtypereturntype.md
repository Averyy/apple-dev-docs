# validRequestor(forSendType:returnType:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to determine what services are available.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)

#### Return Value

If the receiver can place data of `sendType` on the pasteboard and receive data of `returnType`, it should return `self`; otherwise it should return either `[super validRequestorForSendType:returnType:]` or `[[self nextResponder] validRequestorForSendType:returnType:]`, which allows an object higher up in the responder chain to have an opportunity to handle the message.

#### Discussion

With each event, and for each service in the Services menu, the application object sends this message up the responder chain with the send and return type for the service being checked. This method is therefore invoked many times per event. The default implementation simply forwards this message to the next responder, ultimately returning `nil`.

Either `sendType` or `returnType`—but not both—may be empty. If `sendType` is empty, the service doesn’t require input from the application requesting the service. If `returnType` is empty, the service doesn’t return data.

## Parameters

- `sendType`: A string identifying the send type of pasteboard data. May be an empty string (see discussion).
- `returnType`: A string identifying the return type of pasteboard data. May be an empty string (see discussion).

## See Also

- [func readSelection(from: NSPasteboard) -> Bool](nsservicesmenurequestor/readselection(from:).md)
  Reads data from the pasteboard and uses it to replace the current selection.
- [func registerServicesMenuSendTypes([NSPasteboard.PasteboardType], returnTypes: [NSPasteboard.PasteboardType])](nsapplication/registerservicesmenusendtypes(_:returntypes:).md)
  Registers the pasteboard types the receiver can send and receive in response to service requests.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nsservicesmenurequestor/writeselection(to:types:).md)
  Writes the current selection to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/validrequestor(forsendtype:returntype:))*