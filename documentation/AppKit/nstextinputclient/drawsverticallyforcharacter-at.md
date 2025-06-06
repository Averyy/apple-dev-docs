# drawsVerticallyForCharacter(at:)

**Framework**: AppKit  
**Kind**: method

Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func drawsVerticallyForCharacter(at charIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the character is rendered vertically; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `charIndex`: The index of the character to test.

## See Also

- [func characterIndex(for: NSPoint) -> Int](nstextinputclient/characterindex(for:).md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](nstextinputclient/firstrect(forcharacterrange:actualrange:).md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](nstextinputclient/baselinedeltaforcharacter(at:).md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](nstextinputclient/firstrect(forcharacterrange:actualrange:).md).
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](nstextinputclient/fractionofdistancethroughglyph(for:).md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/drawsverticallyforcharacter(at:))*