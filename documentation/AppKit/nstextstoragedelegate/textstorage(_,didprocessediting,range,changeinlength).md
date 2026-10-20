# textStorage(_:didProcessEditing:range:changeInLength:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when a text storage object has finished processing edits.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func textStorage(_ textStorage: NSTextStorage, didProcessEditing editedMask: NSTextStorageEditActions, range editedRange: NSRange, changeInLength delta: Int)
```

```objc
- (void) textStorage:(NSTextStorage *) textStorage didProcessEditing:(NSTextStorageEditActions) editedMask range:(NSRange) editedRange changeInLength:(NSInteger) delta;
```

#### Discussion

Sent inside [`processEditing()`](../nstextstorage/processediting%28%29.md) right before notifying layout managers. Delegates can change the attributes.

The delegate can verify the final state of the text storage object; it can’t change the text storage object’s characters without leaving it in an inconsistent state, but if necessary it can change attributes. Note that even in this case it’s possible to put a text storage object into an inconsistent state—for example, by changing the font of a range to one that doesn’t support the characters in that range, such as using a Latin font for Kanji text.

## Parameters

- `textStorage`: The text storage object processing edits.
- `editedMask`: The types of edits done: [`editedAttributes`](../nstextstorageeditactions/editedattributes.md), [`editedCharacters`](../nstextstorageeditactions/editedcharacters.md), or both.
- `editedRange`: The range in the original string (before the edit).
- `delta`: The length delta for the editing changes.

## See Also

### Processing edit actions
- [func textStorage(NSTextStorage, willProcessEditing: NSTextStorageEditActions, range: NSRange, changeInLength: Int)](./textstorage%28_,willprocessediting,range,changeinlength%29.md)
  The method the framework calls when a text storage object is about to process edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstoragedelegate/textstorage(_:didprocessediting:range:changeinlength:))*