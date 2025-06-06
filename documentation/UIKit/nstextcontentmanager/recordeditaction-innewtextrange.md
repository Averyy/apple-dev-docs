# recordEditAction(in:newTextRange:)

**Framework**: UIKit  
**Kind**: method

Records information about an edit action to the transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func recordEditAction(in originalTextRange: NSTextRange, newTextRange: NSTextRange)
```

#### Discussion

The concrete subclass invokes this method for each edit action.

## Parameters

- `originalTextRange`: The range before the action.
- `newTextRange`: The corresponding range after the action.

## See Also

- [var hasEditingTransaction: Bool](nstextcontentmanager/haseditingtransaction.md)
  Indicates there’s an active editing transaction from the primary text layout manager.
- [func performEditingTransaction(() -> Void)](nstextcontentmanager/performeditingtransaction(_:).md)
  Performs an editing transaction and invokes a block upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/recordeditaction(in:newtextrange:))*