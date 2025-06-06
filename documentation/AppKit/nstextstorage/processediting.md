# processEditing()

**Framework**: AppKit  
**Kind**: method

Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func processEditing()
```

#### Discussion

This method is automatically invoked in response to an [`edited(_:range:changeInLength:)`](nstextstorage/edited(_:range:changeinlength:).md) message or an [`endEditing()`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1416707-endediting) message if edits were made within the scope of a [`beginEditing()`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1411853-beginediting) block. You should never need to invoke it directly.

This method begins by posting an [`willProcessEditingNotification`](nstextstorage/willprocesseditingnotification.md) to the default notification center (which results in the delegate receiving a [`textStorage(_:willProcessEditing:range:changeInLength:)`](nstextstoragedelegate/textstorage(_:willprocessediting:range:changeinlength:).md) message). Then it fixes attributes. After this, it posts an [`didProcessEditingNotification`](nstextstorage/didprocesseditingnotification.md) to the default notification center (which results in the delegate receiving a [`textStorage(_:didProcessEditing:range:changeInLength:)`](nstextstoragedelegate/textstorage(_:didprocessediting:range:changeinlength:).md) message). Finally, it sends a [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](nslayoutmanager/textstorage(_:edited:range:changeinlength:invalidatedrange:).md) message to each of the receiver’s layout managers using the argument values provided.

## See Also

- [func edited(NSTextStorageEditActions, range: NSRange, changeInLength: Int)](nstextstorage/edited(_:range:changeinlength:).md)
  Tracks changes made to the text storage object, allowing the text storage to record the full extent of changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/processediting())*