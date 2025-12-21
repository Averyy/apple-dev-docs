# invalidateLayout(forCharacterRange:actualCharacterRange:)

**Framework**: UIKit  
**Kind**: method

Invalidates the layout information for the glyphs that map to the specified character range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func invalidateLayout(forCharacterRange charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer?)
```

#### Discussion

This method has the same effect as [`invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)`](https://developer.apple.com/documentation/AppKit/NSLayoutManager/invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)) with `flag` set to [`false`](https://developer.apple.com/documentation/Swift/false).

This method only invalidates information; it performs no glyph generation or layout. You should rarely need to invoke this method.

## Parameters

- `charRange`: The range of characters to invalidate.
- `actualCharRange`: If not  , on output, the actual range invalidated after any necessary expansion.

## See Also

- [func invalidateDisplay(forCharacterRange: NSRange)](nslayoutmanager/invalidatedisplay(forcharacterrange:).md)
  Invalidates display for the specified character range.
- [func invalidateDisplay(forGlyphRange: NSRange)](nslayoutmanager/invalidatedisplay(forglyphrange:).md)
  Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [func invalidateGlyphs(forCharacterRange: NSRange, changeInLength: Int, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:).md)
  Invalidates and adjusts the glyphs in the specified character range.
- [func processEditing(for: NSTextStorage, edited: NSTextStorage.EditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nslayoutmanager/processediting(for:edited:range:changeinlength:invalidatedrange:).md)
  Notifies the layout manager when an edit action changes the contents of its text storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:))*