# locationForCharacter(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the location of the character at the specified index.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func locationForCharacter(at index: Int) -> CGPoint
```

```objc
- (CGPoint) locationForCharacterAtIndex:(NSInteger) index;
```

## Return Value

A [`CGPoint`](../../CoreFoundation/cgpoint.md) that’s on the upstream edge of the glyph. It’s in the coordinate system relative to the line fragment origin.

## Parameters

- `index`: An integer that represents the position in the text.

## See Also

### Finding specific text
- [func characterIndex(for: CGPoint) -> Int](./characterindex%28for%29.md)
  Returns character index for a point inside the line fragment coordinate system.
- [func fractionOfDistanceThroughGlyph(for: CGPoint) -> CGFloat](./fractionofdistancethroughglyph%28for%29.md)
  Returns character index for a point inside the line fragment coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/locationforcharacter(at:))*