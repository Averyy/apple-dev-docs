# editedMask

**Framework**: AppKit  
**Kind**: property

A mask that describes the kinds of edits pending for the text storage object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var editedMask: NSTextStorageEditActions { get }
```

#### Discussion

This property indicates pending changes for attributes, characters, or both. Use the C bitwise AND operator to test the value against the [`editedAttributes`](nstextstorageeditactions/editedattributes.md) or [`editedCharacters`](nstextstorageeditactions/editedcharacters.md) constants; testing for equality fails if you add additional mask flags later. The text storage object’s associated delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

- [var editedRange: NSRange](nstextstorage/editedrange.md)
  The range of text that contains changes.
- [var changeInLength: Int](nstextstorage/changeinlength.md)
  The difference between the current length of the edited range and its length before editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/editedmask)*