# characterIndex(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the index of the character whose bounding rectangle includes the given point.

**Availability**:
- macOS ?+

## Declaration

```swift
func characterIndex(for point: NSPoint) -> Int
```

#### Return Value

The character index, measured from the start of the receiver’s text storage, of the character containing the given point. Returns `NSNotFound` if the cursor is not within a character’s bounding rectangle.

## Parameters

- `point`: The point to test, in screen coordinates.

## See Also

- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](nstextinputclient/firstrect(forcharacterrange:actualrange:).md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](nstextinputclient/baselinedeltaforcharacter(at:).md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](nstextinputclient/firstrect(forcharacterrange:actualrange:).md).
- [func drawsVerticallyForCharacter(at: Int) -> Bool](nstextinputclient/drawsverticallyforcharacter(at:).md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](nstextinputclient/fractionofdistancethroughglyph(for:).md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/characterindex(for:))*