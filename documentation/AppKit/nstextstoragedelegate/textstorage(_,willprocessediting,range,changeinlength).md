# textStorage(_:willProcessEditing:range:changeInLength:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when a text storage object is about to process edits.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func textStorage(_ textStorage: NSTextStorage, willProcessEditing editedMask: NSTextStorageEditActions, range editedRange: NSRange, changeInLength delta: Int)
```

```objc
- (void) textStorage:(NSTextStorage *) textStorage willProcessEditing:(NSTextStorageEditActions) editedMask range:(NSRange) editedRange changeInLength:(NSInteger) delta;
```

## Discussion

Sent inside [`processEditing()`](../nstextstorage/processediting%28%29.md) right before fixing attributes. Delegates can change the characters or attributes.

The delegate can verify the changed state of the text storage object and make changes to the text storage object’s characters or attributes to enforce whatever constraints it establishes. Programmatic changes don’t cause the object to send this message.

## Parameters

- `textStorage`: The text storage object processing edits.
- `editedMask`: The types of edits to do: [`editedAttributes`](../nstextstorageeditactions/editedattributes.md) [`editedCharacters`](../nstextstorageeditactions/editedcharacters.md), or both.
- `editedRange`: The range in the original string (before the edit).
- `delta`: The length delta for the editing changes.

## See Also

### Processing edit actions
- [func textStorage(NSTextStorage, didProcessEditing: NSTextStorageEditActions, range: NSRange, changeInLength: Int)](./textstorage%28_,didprocessediting,range,changeinlength%29.md)
  The method the framework calls when a text storage object has finished processing edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstoragedelegate/textstorage(_:willprocessediting:range:changeinlength:))*