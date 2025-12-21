# contextMenuKeyDown(_:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
func contextMenuKeyDown(_ event: NSEvent)
```

#### Discussion

Handle a key event that should present a context menu at the user focus.

Most applications should not override this method. Instead, you should customize the context menu displayed from a keyboard event by implementing `menuForEvent:` and `selectionAnchorRect`, or `showContextMenuForSelection:`, rather than this method.

You should only override this method when you do not want the system-provided default behavior for the context menu hotkey, either for a specific key combination, or for the hotkey in general. For example, if your application already provides a different behavior for control-Return (the default context menu hotkey definition), and you want to preserve that behavior, you should override this method to handle that specific key combination, and then return without calling `super`. Note that the user may customize the hotkey to a different key combination, so in this example, if any other key combination is passed to your method, you would call `super`.

An implementation of this method should call `[super contextMenuKeyDown:event]` to pass the request up the responder chain. If the message reaches the application object, NSApplication’s implementation of this method will send `showContextMenuForSelection:` to the responder chain. If you do not call `super`, then no further handling of the key event will be performed.

> **Note**: In some cases, `showContextMenuForSelection:` will be called without a prior call to `contextMenuKeyDown:`. This occurs when a view receives an Accessibility ShowMenu action, or when the user has created a Cocoa Text key binding to map a different key combination to the `showContextMenuForSelection:` action.

## Parameters

- `event`: The key down event that matches the system-wide context menu hotkey combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/contextmenukeydown(_:))*