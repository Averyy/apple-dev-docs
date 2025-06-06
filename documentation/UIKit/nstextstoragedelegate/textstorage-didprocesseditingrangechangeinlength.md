# textStorage(_:didProcessEditing:range:changeInLength:)

**Framework**: UIKit  
**Kind**: method

The method the framework calls when a text storage object has finished processing edits.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
optional func textStorage(_ textStorage: NSTextStorage, didProcessEditing editedMask: NSTextStorage.EditActions, range editedRange: NSRange, changeInLength delta: Int)
```

#### Discussion

Sent inside [`processEditing()`](nstextstorage/processediting().md) right before notifying layout managers. Delegates can change the attributes.

The delegate can verify the final state of the text storage object; it can’t change the text storage object’s characters without leaving it in an inconsistent state, but if necessary it can change attributes. Note that even in this case it’s possible to put a text storage object into an inconsistent state—for example, by changing the font of a range to one that doesn’t support the characters in that range, such as using a Latin font for Kanji text.

## Parameters

- `textStorage`: The text storage object processing edits.
- `editedMask`: The types of edits done:  ,  , or both.
- `editedRange`: The range in the original string (before the edit).
- `delta`: The length delta for the editing changes.

## See Also

- [func textStorage(NSTextStorage, willProcessEditing: NSTextStorage.EditActions, range: NSRange, changeInLength: Int)](nstextstoragedelegate/textstorage(_:willprocessediting:range:changeinlength:).md)
  The method the framework calls when a text storage object is about to process edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstoragedelegate/textstorage(_:didprocessediting:range:changeinlength:))*