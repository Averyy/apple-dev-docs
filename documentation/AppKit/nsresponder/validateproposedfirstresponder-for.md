# validateProposedFirstResponder(_:for:)

**Framework**: AppKit  
**Kind**: method

Allows controls to determine when they should become first responder.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func validateProposedFirstResponder(_ responder: NSResponder, for event: NSEvent?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the control should become first responder, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Some controls, such as `NSTextField`, should only become first responder when the enclosing NSTableView/NSBrowser indicates that the view can begin editing. It is up to the particular control that wants to be validated to call this method in its [`mouseDown(with:)`](nscontrol/mousedown(with:).md) method (or perhaps at another time) to determine if it should attempt to become the first responder or not.

The [`NSTableView`](nstableview.md), [`NSOutlineView`](nsoutlineview.md), and [`NSBrowser`](nsbrowser.md) classes implement this to allow first responder status only if the responder is a view in a selected row. It also delays the first responder assignment if a `doubleAction` may be invoked.

The default implementation returns [`true`](https://developer.apple.com/documentation/swift/true) when there is no [`nextResponder`](nsresponder/nextresponder.md) set, otherwise, it is forwarded up the responder chain.

## Parameters

- `responder`: The first responder.
- `event`: The event to validate. May be   if there is no applicable event.

## See Also

- [var acceptsFirstResponder: Bool](nsresponder/acceptsfirstresponder.md)
  A Boolean value that indicates whether the responder accepts first responder status.
- [func becomeFirstResponder() -> Bool](nsresponder/becomefirstresponder.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](nswindow.md).
- [func resignFirstResponder() -> Bool](nsresponder/resignfirstresponder.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/validateproposedfirstresponder(_:for:))*