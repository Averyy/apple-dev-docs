# NSTextStorageDelegate

**Framework**: UIKit  
**Kind**: protocol

The optional methods that delegates of text storage objects implement to handle text-edit processing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol NSTextStorageDelegate : NSObjectProtocol
```

## Topics

### Processing edit actions
- [func textStorage(NSTextStorage, willProcessEditing: NSTextStorage.EditActions, range: NSRange, changeInLength: Int)](nstextstoragedelegate/textstorage(_:willprocessediting:range:changeinlength:).md)
  The method the framework calls when a text storage object is about to process edits.
- [func textStorage(NSTextStorage, didProcessEditing: NSTextStorage.EditActions, range: NSRange, changeInLength: Int)](nstextstoragedelegate/textstorage(_:didprocessediting:range:changeinlength:).md)
  The method the framework calls when a text storage object has finished processing edits.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSTextStorageDelegate)?](nstextstorage/delegate.md)
  The delegate for the text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstoragedelegate)*