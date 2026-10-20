# NSTextSelectionManager.Delegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that manage text selection state and let you customize selection behavior.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

```objc
@protocol NSTextSelectionManagerDelegate <NSObject>
```

#### Overview

Delegates are responsible for managing the text selection state and can customize selection behavior by implementing optional methods.

## Topics

### Instance Properties
- [var textSelection: NSTextSelection?](./delegate-swift.protocol/textselection.md)
  The current text selection.
### Instance Methods
- [func selectionManager(NSTextSelectionManager, frameOfTextContainerAt: NSPoint) -> NSRect](./delegate-swift.protocol/selectionmanager%28_,frameoftextcontainerat%29.md)
  Returns the frame of the text container at the specified point.
- [func selectionManager(NSTextSelectionManager, locationOfTextContainerAt: NSPoint) -> (any NSTextLocation)?](./delegate-swift.protocol/selectionmanager%28_,locationoftextcontainerat%29.md)
  Returns the text location of the text container at the specified point.
- [func selectionManager(NSTextSelectionManager, makeDraggingSession: NSGestureRecognizer) -> NSDraggingSession?](./delegate-swift.protocol/selectionmanager%28_,makedraggingsession%29.md)
  Creates and returns a dragging session for the specified gesture recognizer.
- [func selectionManager(NSTextSelectionManager, shouldBeginSelectionAt: NSPoint) -> Bool](./delegate-swift.protocol/selectionmanager%28_,shouldbeginselectionat%29.md)
  Asks the delegate whether a selection can begin at the specified point.
- [func selectionManagerDidEndSelection(NSTextSelectionManager)](./delegate-swift.protocol/selectionmanagerdidendselection%28_%29.md)
  Tells the delegate that a selection gesture has ended.
- [func selectionManagerWillBeginSelection(NSTextSelectionManager)](./delegate-swift.protocol/selectionmanagerwillbeginselection%28_%29.md)
  Tells the delegate that a selection gesture is about to begin.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting a delegate
- [var delegate: (any NSTextSelectionManager.Delegate)?](./delegate-swift.property.md)
  The delegate of the text selection manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol)*