# invalidateDisplay(forGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func invalidateDisplay(forGlyphRange glyphRange: NSRange)
```

#### Discussion

You should rarely need to invoke this method.

## Parameters

- `glyphRange`: The range of glyphs to invalidate.

## See Also

- [func invalidateDisplay(forCharacterRange: NSRange)](nslayoutmanager/invalidatedisplay(forcharacterrange:).md)
  Invalidates display for the specified character range.
- [func invalidateGlyphs(forCharacterRange: NSRange, changeInLength: Int, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:).md)
  Invalidates and adjusts the glyphs in the specified character range.
- [func invalidateLayout(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:).md)
  Invalidates the layout information for the glyphs that map to the specified character range.
- [func processEditing(for: NSTextStorage, edited: NSTextStorageEditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nslayoutmanager/processediting(for:edited:range:changeinlength:invalidatedrange:).md)
  Notifies the layout manager when an edit action changes the contents of its text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/invalidatedisplay(forglyphrange:))*