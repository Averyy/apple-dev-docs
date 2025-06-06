# changeInLength

**Framework**: UIKit  
**Kind**: property

The difference between the current length of the edited range and its length before editing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var changeInLength: Int { get }
```

#### Discussion

This property reflects difference between the current length of the edited range and its length before editing began—that is, before the first call to the [`beginEditing()`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1411853-beginediting) method or a single call to the[`edited(_:range:changeInLength:)`](nstextstorage/edited(_:range:changeinlength:).md) method. This difference is accumulated with each call to the [`edited(_:range:changeInLength:)`](nstextstorage/edited(_:range:changeinlength:).md) method, until the changes are finally processed.

The text storage object’s delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

- [var editedMask: NSTextStorage.EditActions](nstextstorage/editedmask.md)
  A mask that describes the kinds of edits pending for the text storage object.
- [var editedRange: NSRange](nstextstorage/editedrange.md)
  The range of text that contains changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/changeinlength)*