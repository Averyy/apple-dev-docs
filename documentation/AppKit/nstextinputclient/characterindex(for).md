# characterIndex(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the index of the character whose bounding rectangle includes the given point.

**Availability**:
- macOS

## Declaration

```swift
func characterIndex(for point: NSPoint) -> Int
```

```objc
- (NSUInteger) characterIndexForPoint:(NSPoint) point;
```

#### Return Value

The character index, measured from the start of the receiver’s text storage, of the character containing the given point. Returns `NSNotFound` if the cursor is not within a character’s bounding rectangle.

## Parameters

- `point`: The point to test, in screen coordinates.

## See Also

### Getting character coordinates
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](./firstrect%28forcharacterrange,actualrange%29.md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](./baselinedeltaforcharacter%28at%29.md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](./firstrect%28forcharacterrange,actualrange%29.md).
- [func drawsVerticallyForCharacter(at: Int) -> Bool](./drawsverticallyforcharacter%28at%29.md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](./fractionofdistancethroughglyph%28for%29.md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/characterindex(for:))*