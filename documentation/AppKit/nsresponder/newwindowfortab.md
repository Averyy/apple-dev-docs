# newWindowForTab(_:)

**Framework**: AppKit  
**Kind**: method

Creates a new window to show as a tab in a tabbed window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@IBAction
@MainActor func newWindowForTab(_ sender: Any?)
```

#### Discussion

The system automatically calls this method to create a window for a new tab when the user clicks the plus button in a tabbed window. The system shows a plus button on a tabbed window only if this method exists on one of the following objects:

- In an [`NSDocumentController`](nsdocumentcontroller.md) subclass
- In the responder chain starting at [`NSWindow`](nswindow.md), such as [`NSWindow`](nswindow.md), the window delegate, the window controller, the [`NSApplication`](nsapplication.md) delegate, and so on

## Parameters

- `sender`: The sender of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/newwindowfortab(_:))*