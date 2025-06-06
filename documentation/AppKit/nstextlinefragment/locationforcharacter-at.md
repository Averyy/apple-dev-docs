# locationForCharacter(at:)

**Framework**: AppKit  
**Kind**: method

Returns the location of the character at the specified index.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func locationForCharacter(at index: Int) -> CGPoint
```

#### Return Value

A [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) that’s on the upstream edge of the glyph. It’s in the coordinate system relative to the line fragment origin.

## Parameters

- `index`: An integer that represents the position in the text.

## See Also

- [func characterIndex(for: CGPoint) -> Int](nstextlinefragment/characterindex(for:).md)
  Returns character index for a point inside the line fragment coordinate system.
- [func fractionOfDistanceThroughGlyph(for: CGPoint) -> CGFloat](nstextlinefragment/fractionofdistancethroughglyph(for:).md)
  Returns character index for a point inside the line fragment coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment/locationforcharacter(at:))*