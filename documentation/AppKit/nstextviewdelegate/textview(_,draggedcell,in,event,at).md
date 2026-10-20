# textView(_:draggedCell:in:event:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the user attempts to drag a cell.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, draggedCell cell: any NSTextAttachmentCellProtocol, in rect: NSRect, event: NSEvent, at charIndex: Int)
```

```objc
- (void) textView:(NSTextView *) view draggedCell:(id<NSTextAttachmentCell>) cell inRect:(NSRect) rect event:(NSEvent *) event atIndex:(NSUInteger) charIndex;
```

#### Discussion

The delegate can use this message as its cue to initiate a dragging operation.

## Parameters

- `view`: The text view sending the message.
- `cell`: The cell being dragged.
- `rect`: The rectangle from which the cell was dragged.
- `event`: The mouse-down event that preceded the mouse-dragged event.
- `charIndex`: The character position where the mouse button was clicked.

## See Also

### Related Documentation
- [func dragFile(String, from: NSRect, slideBack: Bool, event: NSEvent) -> Bool](../nsview/dragfile%28_,from,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:draggedcell:in:event:at:))*