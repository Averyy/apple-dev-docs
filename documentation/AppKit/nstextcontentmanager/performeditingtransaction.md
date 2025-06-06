# performEditingTransaction(_:)

**Framework**: AppKit  
**Kind**: method

Performs an editing transaction and invokes a block upon completion.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func performEditingTransaction(_ transaction: () -> Void)
```

#### Discussion

The primary [`NSTextLayoutManager`](nstextlayoutmanager.md) controlling the active editing transaction invokes this method. It’s possible to nest multiple editing transactions. The outer most transaction toggles `hasEditingTransaction` and sends synchronization messages if enabled after invoking a transaction.

## Parameters

- `transaction`: The editing transaction.

## See Also

- [var hasEditingTransaction: Bool](nstextcontentmanager/haseditingtransaction.md)
  Indicates there’s an active editing transaction from the primary text layout manager.
- [func recordEditAction(in: NSTextRange, newTextRange: NSTextRange)](nstextcontentmanager/recordeditaction(in:newtextrange:).md)
  Records information about an edit action to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/performeditingtransaction(_:))*