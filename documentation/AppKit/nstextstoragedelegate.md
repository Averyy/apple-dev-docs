# NSTextStorageDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The optional methods that delegates of text storage objects implement to handle text-edit processing.

**Availability**:
- macOS 10.11+

## Declaration

```swift
protocol NSTextStorageDelegate : NSObjectProtocol
```

```objc
@protocol NSTextStorageDelegate <NSObject>
```

## Topics

### Processing edit actions
- [func textStorage(NSTextStorage, willProcessEditing: NSTextStorageEditActions, range: NSRange, changeInLength: Int)](./nstextstoragedelegate/textstorage%28_,willprocessediting,range,changeinlength%29.md)
  The method the framework calls when a text storage object is about to process edits.
- [func textStorage(NSTextStorage, didProcessEditing: NSTextStorageEditActions, range: NSRange, changeInLength: Int)](./nstextstoragedelegate/textstorage%28_,didprocessediting,range,changeinlength%29.md)
  The method the framework calls when a text storage object has finished processing edits.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Processing the editing actions
- [var delegate: (any NSTextStorageDelegate)?](./nstextstorage/delegate.md)
  The delegate for the text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstoragedelegate)*