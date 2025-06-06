# hasEditingTransaction

**Framework**: UIKit  
**Kind**: property

Indicates there’s an active editing transaction from the primary text layout manager.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var hasEditingTransaction: Bool { get }
```

#### Discussion

When this property is `true`, there’s an active editing transaction from the `primaryTextLayoutManager`. The synchronization operations to nonprimary text layout managers and the backing store block (or fail when synchronous) while this property is `true`. Avoid accessing the elements from a nonprimary text layout manager while this values is `true`.

This property is KVO-compliant.

## See Also

- [func performEditingTransaction(() -> Void)](nstextcontentmanager/performeditingtransaction(_:).md)
  Performs an editing transaction and invokes a block upon completion.
- [func recordEditAction(in: NSTextRange, newTextRange: NSTextRange)](nstextcontentmanager/recordeditaction(in:newtextrange:).md)
  Records information about an edit action to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/haseditingtransaction)*