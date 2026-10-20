# NSTextStorageObserving

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

Optional methods that delegates implement to handle editing and transaction processing.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextStorageObserving : NSObjectProtocol
```

```objc
@protocol NSTextStorageObserving <NSObject>
```

## Topics

### Accessing the text storage
- [var textStorage: NSTextStorage?](./nstextstorageobserving/textstorage.md)
### Managing the editing process
- [func performEditingTransaction(for: NSTextStorage, using: () -> Void)](./nstextstorageobserving/performeditingtransaction%28for,using%29.md)
- [func processEditing(for: NSTextStorage, edited: NSTextStorageEditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](./nstextstorageobserving/processediting%28for,edited,range,changeinlength,invalidatedrange%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTextContentStorage](./nstextcontentstorage.md)

## See Also

### Accessing the storage controller
- [var textStorageObserver: (any NSTextStorageObserving)?](./nstextstorage/textstorageobserver.md)
  The observer for the text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageobserving)*