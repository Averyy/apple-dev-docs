# characterIndex(for:)

**Framework**: UIKit  
**Kind**: method

Returns character index for a point inside the line fragment coordinate system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func characterIndex(for point: CGPoint) -> Int
```

#### Return Value

An integer that represents the character index at `point`.

## Parameters

- `point`: The distance is from the upstream edge.

## See Also

- [func fractionOfDistanceThroughGlyph(for: CGPoint) -> CGFloat](nstextlinefragment/fractionofdistancethroughglyph(for:).md)
  Returns character index for a point inside the line fragment coordinate system.
- [func locationForCharacter(at: Int) -> CGPoint](nstextlinefragment/locationforcharacter(at:).md)
  Returns the location of the character at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/characterindex(for:))*