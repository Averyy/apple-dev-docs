# NSTextStorageObserving

**Framework**: UIKit  
**Kind**: protocol

Optional methods that delegates implement to handle editing and transaction processing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSTextStorageObserving : NSObjectProtocol
```

## Topics

### Accessing the text storage
- [var textStorage: NSTextStorage?](nstextstorageobserving/textstorage.md)
### Managing the editing process
- [func performEditingTransaction(for: NSTextStorage, using: () -> Void)](nstextstorageobserving/performeditingtransaction(for:using:).md)
- [func processEditing(for: NSTextStorage, edited: NSTextStorage.EditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextContentStorage](nstextcontentstorage.md)

## See Also

- [var textStorageObserver: (any NSTextStorageObserving)?](nstextstorage/textstorageobserver.md)
  The observer for the text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorageobserving)*