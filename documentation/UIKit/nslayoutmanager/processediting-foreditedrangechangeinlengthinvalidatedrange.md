# processEditing(for:edited:range:changeInLength:invalidatedRange:)

**Framework**: UIKit  
**Kind**: method

Notifies the layout manager when an edit action changes the contents of its text storage object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func processEditing(for textStorage: NSTextStorage, edited editMask: NSTextStorage.EditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

#### Discussion

The [`processEditing()`](nstextstorage/processediting().md) method of [`NSTextStorage`](nstextstorage.md) calls this method to notify the layout manager of an edit action. Layout managers must not change the contents of the text storage during the execution of this message.

## Parameters

- `textStorage`: The text storage object processing edits.
- `editMask`: The types of edits done:  ,  , or both.
- `newCharRange`: The range in the final string that was explicitly edited.
- `delta`: The length delta for the editing changes.
- `invalidatedCharRange`: The range of characters that changed as a result of attribute fixing. This invalidated range is either equal to   or larger.

## See Also

- [func invalidateDisplay(forCharacterRange: NSRange)](nslayoutmanager/invalidatedisplay(forcharacterrange:).md)
  Invalidates display for the specified character range.
- [func invalidateDisplay(forGlyphRange: NSRange)](nslayoutmanager/invalidatedisplay(forglyphrange:).md)
  Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [func invalidateGlyphs(forCharacterRange: NSRange, changeInLength: Int, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:).md)
  Invalidates and adjusts the glyphs in the specified character range.
- [func invalidateLayout(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:).md)
  Invalidates the layout information for the glyphs that map to the specified character range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/processediting(for:edited:range:changeinlength:invalidatedrange:))*