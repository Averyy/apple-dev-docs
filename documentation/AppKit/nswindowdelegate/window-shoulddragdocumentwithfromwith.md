# window(_:shouldDragDocumentWith:from:with:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether a user can drag the document icon from the window’s title bar.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, shouldDragDocumentWith event: NSEvent, from dragImageLocation: NSPoint, with pasteboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the drag to proceed; [`false`](https://developer.apple.com/documentation/Swift/false) to prevent it. Before turning no the delegate can implement its own dragging behavior as described below.

#### Discussion

Implementing this method enables an application to customize the process of dragging the window’s document icon. The delegate can prohibit the drag by returning [`false`](https://developer.apple.com/documentation/Swift/false). Before returning [`false`](https://developer.apple.com/documentation/Swift/false), the delegate can implement its own dragging behavior using  [`drag(_:at:offset:event:pasteboard:source:slideBack:)`](nswindow/drag(_:at:offset:event:pasteboard:source:slideback:).md).

Alternatively, the delegate can enable a drag by returning [`true`](https://developer.apple.com/documentation/Swift/true), for example, to override the default `NSWindow` behavior of prohibiting the drag of an edited document. In addition, the delegate can customize the pasteboard contents before returning [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `window`: The window containing the document icon the user wants to drag.
- `event`: The left-mouse down event that triggered the dragging operation.
- `dragImageLocation`: The location of the origin of the document icon, in window coordinates, when the user started the dragging operation.
- `pasteboard`: The pasteboard containing the contents of the document, which the delegate can modify.

## See Also

- [var representedURL: URL?](nswindow/representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:shoulddragdocumentwith:from:with:))*