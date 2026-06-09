# selectionManagerDidEndSelection(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that a selection gesture has ended.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func selectionManagerDidEndSelection(_ selectionManager: NSTextSelectionManager)
```

#### Discussion

The selection manager calls this method after finishing processing a selection gesture, such as when the user releases the mouse button.

## Parameters

- `selectionManager`: The selection manager that ended selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/selectionmanagerdidendselection(_:))*