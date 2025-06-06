# firstResponder

**Framework**: AppKit  
**Kind**: property

The window’s first responder.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var firstResponder: NSResponder? { get }
```

#### Discussion

The first responder is usually the first object in a responder chain to receive an event or action message. In most cases, the first responder is a view object that the user selects or activates with the mouse or keyboard.

You can use the [`firstResponder`](nswindow/firstresponder.md) property in custom subclasses of responder classes ([`NSWindow`](nswindow.md), [`NSApplication`](nsapplication.md), [`NSView`](nsview.md), and subclasses) to determine if an instance of the subclass is currently the first responder. You can also use it to help locate a text field that currently has first-responder status. For more on this subject, see [`Event Handling Basics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventHandlingBasics/EventHandlingBasics.html#//apple_ref/doc/uid/10000060i-CH5). This property is key-value observing compliant.

## See Also

- [var acceptsFirstResponder: Bool](nsresponder/acceptsfirstresponder.md)
  A Boolean value that indicates whether the responder accepts first responder status.
- [var initialFirstResponder: NSView?](nswindow/initialfirstresponder.md)
  The view that’s made first responder (also called the key view) the first time the window is placed onscreen.
- [func makeFirstResponder(NSResponder?) -> Bool](nswindow/makefirstresponder(_:).md)
  Attempts to make a given responder the first responder for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/firstresponder)*