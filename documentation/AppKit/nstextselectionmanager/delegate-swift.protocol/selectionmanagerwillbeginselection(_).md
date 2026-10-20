# selectionManagerWillBeginSelection(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a selection gesture is about to begin.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func selectionManagerWillBeginSelection(_ selectionManager: NSTextSelectionManager)
```

```objc
- (void) selectionManagerWillBeginSelection:(NSTextSelectionManager *) selectionManager;
```

#### Discussion

The selection manager calls this method after `selectionManager:shouldBeginSelectionAtPoint:` returns `YES` (or if that method isn’t implemented) and before any selection changes are made.

## Parameters

- `selectionManager`: The selection manager that is about to begin selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanagerwillbeginselection(_:))*