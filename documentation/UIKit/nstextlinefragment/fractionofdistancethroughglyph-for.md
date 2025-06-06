# fractionOfDistanceThroughGlyph(for:)

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
func fractionOfDistanceThroughGlyph(for point: CGPoint) -> CGFloat
```

#### Return Value

The fraction of distance from the upstream edge.

## Parameters

- `point`: A   that represents the point inside the line fragment.

## See Also

- [func characterIndex(for: CGPoint) -> Int](nstextlinefragment/characterindex(for:).md)
  Returns character index for a point inside the line fragment coordinate system.
- [func locationForCharacter(at: Int) -> CGPoint](nstextlinefragment/locationforcharacter(at:).md)
  Returns the location of the character at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/fractionofdistancethroughglyph(for:))*