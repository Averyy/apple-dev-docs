# NSTextStorageObserving

**Framework**: AppKit  
**Kind**: protocol

Optional methods that delegates implement to handle editing and transaction processing.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextStorageObserving : NSObjectProtocol
```

## Topics

### Accessing the text storage
- [var textStorage: NSTextStorage?](nstextstorageobserving/textstorage.md)
### Managing the editing process
- [func performEditingTransaction(for: NSTextStorage, using: () -> Void)](nstextstorageobserving/performeditingtransaction(for:using:).md)
- [func processEditing(for: NSTextStorage, edited: NSTextStorageEditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextContentStorage](nstextcontentstorage.md)

## See Also

- [var textStorageObserver: (any NSTextStorageObserving)?](nstextstorage/textstorageobserver.md)
  The observer for the text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageobserving)*