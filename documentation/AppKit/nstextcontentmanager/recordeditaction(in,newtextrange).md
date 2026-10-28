# recordEditAction(in:newTextRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Records information about an edit action to the transaction.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func recordEditAction(in originalTextRange: NSTextRange, newTextRange: NSTextRange)
```

```objc
- (void) recordEditActionInRange:(NSTextRange *) originalTextRange newTextRange:(NSTextRange *) newTextRange;
```

## Discussion

The concrete subclass invokes this method for each edit action.

## Parameters

- `originalTextRange`: The range before the action.
- `newTextRange`: The corresponding range after the action.

## See Also

### Performing transactions
- [var hasEditingTransaction: Bool](./haseditingtransaction.md)
  Indicates there’s an active editing transaction from the primary text layout manager.
- [func performEditingTransaction(() -> Void)](./performeditingtransaction%28_%29.md)
  Performs an editing transaction and invokes a block upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/recordeditaction(in:newtextrange:))*