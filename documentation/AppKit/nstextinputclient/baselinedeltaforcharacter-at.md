# baselineDeltaForCharacter(at:)

**Framework**: AppKit  
**Kind**: method

Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](nstextinputclient/firstrect(forcharacterrange:actualrange:).md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func baselineDeltaForCharacter(at anIndex: Int) -> CGFloat
```

#### Return Value

The vertical distance, in points, between the baseline of the character at `anIndex` and the rectangle origin.

#### Discussion

Implementation of this method is optional. This information allows the caller to determine finer-grained character positioning within the text storage of the text view adopting `NSTextInputClient`.

## Parameters

- `anIndex`: Index of the character whose baseline is tested.

## See Also

- [func characterIndex(for: NSPoint) -> Int](nstextinputclient/characterindex(for:).md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](nstextinputclient/firstrect(forcharacterrange:actualrange:).md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func drawsVerticallyForCharacter(at: Int) -> Bool](nstextinputclient/drawsverticallyforcharacter(at:).md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](nstextinputclient/fractionofdistancethroughglyph(for:).md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/baselinedeltaforcharacter(at:))*