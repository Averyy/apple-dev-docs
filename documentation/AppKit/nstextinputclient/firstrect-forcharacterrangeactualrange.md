# firstRect(forCharacterRange:actualRange:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the first logical boundary rectangle for characters in the given range.

**Availability**:
- macOS ?+

## Declaration

```swift
func firstRect(forCharacterRange range: NSRange, actualRange: NSRangePointer?) -> NSRect
```

#### Return Value

The boundary rectangle for the given range of characters, in screen coordinates. The rectangle’s  `size` value can be negative if the text flows to the left.

#### Discussion

If `aRange` spans multiple lines of text in the text view, the rectangle returned is the one surrounding the characters in the first line. In that case `actualRange` contains the range covered by the first rect, so you can query all line fragments by invoking this method repeatedly. If the length of `aRange` is 0 (as it would be if there is nothing selected at the insertion point), the rectangle coincides with the insertion point, and its width is 0.

## Parameters

- `range`: The character range whose boundary rectangle is returned.
- `actualRange`: If non- , contains the character range corresponding to the returned area if it was adjusted, for example, to a grapheme cluster boundary or characters in the first line fragment.

## See Also

- [func characterIndex(for: NSPoint) -> Int](nstextinputclient/characterindex(for:).md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](nstextinputclient/baselinedeltaforcharacter(at:).md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](nstextinputclient/firstrect(forcharacterrange:actualrange:).md).
- [func drawsVerticallyForCharacter(at: Int) -> Bool](nstextinputclient/drawsverticallyforcharacter(at:).md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](nstextinputclient/fractionofdistancethroughglyph(for:).md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/firstrect(forcharacterrange:actualrange:))*