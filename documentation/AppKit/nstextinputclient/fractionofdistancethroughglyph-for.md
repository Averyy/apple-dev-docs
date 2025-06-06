# fractionOfDistanceThroughGlyph(for:)

**Framework**: AppKit  
**Kind**: method

Returns the fraction of the distance from the left side of the character to the right side that a given point lies.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func fractionOfDistanceThroughGlyph(for point: NSPoint) -> CGFloat
```

#### Return Value

The fraction of the distance `aPoint` is through the glyph in which it lies. May be 0 or 1 if `aPoint` is not within the bounding rectangle of a glyph (0 if the point is to the left or above the glyph; 1 if it’s to the right or below).

#### Discussion

Implementation of this method is optional. This allows caller to perform precise selection handling.

For purposes such as dragging out a selection or placing the insertion point, a partial percentage less than or equal to 0.5 indicates that `aPoint` should be considered as falling before the glyph; a partial percentage greater than 0.5 indicates that it should be considered as falling after the glyph. If the nearest glyph doesn’t lie under `aPoint` at all (for example, if `aPoint` is beyond the beginning or end of a line), this ratio is 0 or 1.

For example, if the glyph stream contains the glyphs “A” and “b”, with the width of “A” being 13 points, and `aPoint` is 8 points from the left side of “A”, then the fraction of the distance is 8/13, or 0.615. In this case, the `aPoint` should be considered as falling between “A” and “b” for purposes such as dragging out a selection or placing the insertion point.

## Parameters

- `point`: The point to test.

## See Also

- [func characterIndex(for: NSPoint) -> Int](nstextinputclient/characterindex(for:).md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](nstextinputclient/firstrect(forcharacterrange:actualrange:).md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](nstextinputclient/baselinedeltaforcharacter(at:).md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](nstextinputclient/firstrect(forcharacterrange:actualrange:).md).
- [func drawsVerticallyForCharacter(at: Int) -> Bool](nstextinputclient/drawsverticallyforcharacter(at:).md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/fractionofdistancethroughglyph(for:))*