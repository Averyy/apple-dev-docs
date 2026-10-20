# baselineDeltaForCharacter(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](./firstrect%28forcharacterrange,actualrange%29.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func baselineDeltaForCharacter(at anIndex: Int) -> CGFloat
```

```objc
- (CGFloat) baselineDeltaForCharacterAtIndex:(NSUInteger) anIndex;
```

#### Return Value

The vertical distance, in points, between the baseline of the character at `anIndex` and the rectangle origin.

#### Discussion

Implementation of this method is optional. This information allows the caller to determine finer-grained character positioning within the text storage of the text view adopting `NSTextInputClient`.

## Parameters

- `anIndex`: Index of the character whose baseline is tested.

## See Also

### Getting character coordinates
- [func characterIndex(for: NSPoint) -> Int](./characterindex%28for%29.md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](./firstrect%28forcharacterrange,actualrange%29.md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func drawsVerticallyForCharacter(at: Int) -> Bool](./drawsverticallyforcharacter%28at%29.md)
  Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](./fractionofdistancethroughglyph%28for%29.md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/baselinedeltaforcharacter(at:))*