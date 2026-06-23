# NSTextSelectionManager.Delegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that manage text selection state and let you customize selection behavior.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

#### Overview

Delegates are responsible for managing the text selection state and can customize selection behavior by implementing optional methods.

## Topics

### Instance Properties
- [var textSelection: NSTextSelection?](nstextselectionmanager/delegate-swift.protocol/textselection.md)
  The current text selection.
### Instance Methods
- [func selectionManager(NSTextSelectionManager, frameOfTextContainerAt: NSPoint) -> NSRect](nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:frameoftextcontainerat:).md)
  Returns the frame of the text container at the specified point.
- [func selectionManager(NSTextSelectionManager, locationOfTextContainerAt: NSPoint) -> (any NSTextLocation)?](nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:locationoftextcontainerat:).md)
  Returns the text location of the text container at the specified point.
- [func selectionManager(NSTextSelectionManager, makeDraggingSession: NSGestureRecognizer) -> NSDraggingSession?](nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:makedraggingsession:).md)
  Creates and returns a dragging session for the specified gesture recognizer.
- [func selectionManager(NSTextSelectionManager, shouldBeginSelectionAt: NSPoint) -> Bool](nstextselectionmanager/delegate-swift.protocol/selectionmanager(_:shouldbeginselectionat:).md)
  Asks the delegate whether a selection can begin at the specified point.
- [func selectionManagerDidEndSelection(NSTextSelectionManager)](nstextselectionmanager/delegate-swift.protocol/selectionmanagerdidendselection(_:).md)
  Tells the delegate that a selection gesture has ended.
- [func selectionManagerWillBeginSelection(NSTextSelectionManager)](nstextselectionmanager/delegate-swift.protocol/selectionmanagerwillbeginselection(_:).md)
  Tells the delegate that a selection gesture is about to begin.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSTextSelectionManager.Delegate)?](nstextselectionmanager/delegate-swift.property.md)
  The delegate of the text selection manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol)*