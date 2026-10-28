# drawsVerticallyForCharacter(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the text input management system whether the protocol-conforming client renders the character at the given index vertically.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func drawsVerticallyForCharacter(at charIndex: Int) -> Bool
```

```objc
- (BOOL) drawsVerticallyForCharacterAtIndex:(NSUInteger) charIndex;
```

## Return Value

[`true`](../../Swift/true.md) if the character is rendered vertically; otherwise [`false`](../../Swift/false.md).

## Parameters

- `charIndex`: The index of the character to test.

## See Also

### Getting character coordinates
- [func characterIndex(for: NSPoint) -> Int](./characterindex%28for%29.md)
  Returns the index of the character whose bounding rectangle includes the given point.
- [func firstRect(forCharacterRange: NSRange, actualRange: NSRangePointer?) -> NSRect](./firstrect%28forcharacterrange,actualrange%29.md)
  Returns the first logical boundary rectangle for characters in the given range.
- [func baselineDeltaForCharacter(at: Int) -> CGFloat](./baselinedeltaforcharacter%28at%29.md)
  Returns the baseline position of a given character relative to the origin of rectangle returned by [`firstRect(forCharacterRange:actualRange:)`](./firstrect%28forcharacterrange,actualrange%29.md).
- [func fractionOfDistanceThroughGlyph(for: NSPoint) -> CGFloat](./fractionofdistancethroughglyph%28for%29.md)
  Returns the fraction of the distance from the left side of the character to the right side that a given point lies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/drawsverticallyforcharacter(at:))*