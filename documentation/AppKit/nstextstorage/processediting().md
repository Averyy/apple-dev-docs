# processEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func processEditing()
```

```objc
- (void) processEditing;
```

## Discussion

This method is automatically invoked in response to an [`edited(_:range:changeInLength:)`](./edited%28_,range,changeinlength%29.md) message or an [`endEditing()`](../../Foundation/nsmutableattributedstring/endediting%28%29.md) message if edits were made within the scope of a [`beginEditing()`](../../Foundation/nsmutableattributedstring/beginediting%28%29.md) block. You should never need to invoke it directly.

This method begins by posting an [`willProcessEditingNotification`](./willprocesseditingnotification.md) to the default notification center (which results in the delegate receiving a [`textStorage(_:willProcessEditing:range:changeInLength:)`](../nstextstoragedelegate/textstorage%28_,willprocessediting,range,changeinlength%29.md) message). Then it fixes attributes. After this, it posts an [`didProcessEditingNotification`](./didprocesseditingnotification.md) to the default notification center (which results in the delegate receiving a [`textStorage(_:didProcessEditing:range:changeInLength:)`](../nstextstoragedelegate/textstorage%28_,didprocessediting,range,changeinlength%29.md) message). Finally, it sends a [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](../nslayoutmanager/textstorage%28_,edited,range,changeinlength,invalidatedrange%29.md) message to each of the receiver’s layout managers using the argument values provided.

## See Also

### Managing edits
- [func edited(NSTextStorageEditActions, range: NSRange, changeInLength: Int)](./edited%28_,range,changeinlength%29.md)
  Tracks changes made to the text storage object, allowing the text storage to record the full extent of changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/processediting())*