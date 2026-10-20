# hasEditingTransaction

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates there’s an active editing transaction from the primary text layout manager.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var hasEditingTransaction: Bool { get }
```

```objc
@property (readonly) BOOL hasEditingTransaction;
```

#### Discussion

When this property is `true`, there’s an active editing transaction from the `primaryTextLayoutManager`. The synchronization operations to nonprimary text layout managers and the backing store block (or fail when synchronous) while this property is `true`. Avoid accessing the elements from a nonprimary text layout manager while this values is `true`.

This property is KVO-compliant.

## See Also

### Performing transactions
- [func performEditingTransaction(() -> Void)](./performeditingtransaction%28_%29.md)
  Performs an editing transaction and invokes a block upon completion.
- [func recordEditAction(in: NSTextRange, newTextRange: NSTextRange)](./recordeditaction%28in,newtextrange%29.md)
  Records information about an edit action to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/haseditingtransaction)*