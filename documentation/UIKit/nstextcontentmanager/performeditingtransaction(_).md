# performEditingTransaction(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Performs an editing transaction and invokes a block upon completion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func performEditingTransaction(_ transaction: () -> Void)
```

```objc
- (void) performEditingTransactionUsingBlock:(void (^)()) transaction;
```

## Discussion

The primary [`NSTextLayoutManager`](../nstextlayoutmanager.md) controlling the active editing transaction invokes this method. It’s possible to nest multiple editing transactions. The outer most transaction toggles `hasEditingTransaction` and sends synchronization messages if enabled after invoking a transaction.

## Parameters

- `transaction`: The editing transaction.

## See Also

### Performing transactions
- [var hasEditingTransaction: Bool](./haseditingtransaction.md)
  Indicates there’s an active editing transaction from the primary text layout manager.
- [func recordEditAction(in: NSTextRange, newTextRange: NSTextRange)](./recordeditaction%28in,newtextrange%29.md)
  Records information about an edit action to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/performeditingtransaction(_:))*