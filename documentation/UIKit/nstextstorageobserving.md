# NSTextStorageObserving

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSTextStorageObserving <NSObject>
```

## Topics

### Accessing the text storage
- [var textStorage: NSTextStorage?](./nstextstorageobserving/textstorage.md)
  The document text storage object.
### Managing the editing process
- [func performEditingTransaction(for: NSTextStorage, using: () -> Void)](./nstextstorageobserving/performeditingtransaction%28for,using%29.md)
  Performs an editing transaction on the text storage.
- [func processEditing(for: NSTextStorage, edited: NSTextStorage.EditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](./nstextstorageobserving/processediting%28for,edited,range,changeinlength,invalidatedrange%29.md)
  Notifies the observer that the text storage has been edited.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorageobserving)*