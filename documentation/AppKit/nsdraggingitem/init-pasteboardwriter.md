# init(pasteboardWriter:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a dragging item using the specified content.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(pasteboardWriter: any NSPasteboardWriting)
```

#### Return Value

An initialized NSDraggingItem instance with the specified dragging content.

#### Discussion

When the developer creates an `NSDraggingItem` instance , it is for use with the view method [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md) During the invocation of that method, the `pasteboardWriter` is placed onto the dragging pasteboard for the `NSDraggingSession` that contains the dragging item instance.

The designated initializer.

## Parameters

- `pasteboardWriter`: The object that provides the dragging content. The object must implement the   protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/init(pasteboardwriter:))*