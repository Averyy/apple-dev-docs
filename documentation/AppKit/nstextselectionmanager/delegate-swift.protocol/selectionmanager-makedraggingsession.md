# selectionManager(_:makeDraggingSession:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a dragging session for the specified gesture recognizer.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func selectionManager(_ selectionManager: NSTextSelectionManager, makeDraggingSession gesture: NSGestureRecognizer) -> NSDraggingSession?
```

#### Return Value

A new dragging session, or `nil` to prevent dragging.

#### Discussion

The selection manager calls this method when the user attempts to drag the current text selection. Use this method to customize the dragging behavior, including setting drag data and drag images.

## Parameters

- `selectionManager`: The selection manager requesting the dragging session.
- `gesture`: The gesture recognizer that detected the drag attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:makedraggingsession:))*