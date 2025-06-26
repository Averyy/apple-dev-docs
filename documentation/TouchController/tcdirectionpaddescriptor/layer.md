# layer

**Framework**: Touch Controller  
**Kind**: property

The layer of the direction pad, used for z-sorting.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var layer: simd_int1 { get set }
```

## See Also

- [var anchor: TCTransformAnchor](tcdirectionpaddescriptor/anchor.md)
  The anchor point that the direction pad’s offset is relative to.
- [var colliderType: TCColliderType](tcdirectionpaddescriptor/collidertype.md)
  The type of collider to use for the direction pad.
- [var compositeLabel: TCControlLabel?](tcdirectionpaddescriptor/compositelabel.md)
  A composite control label.
- [var downLabel: TCControlLabel?](tcdirectionpaddescriptor/downlabel.md)
  The label for the down button, if the control is not a composite direction pad.
- [var downVisuals: TCControlVisuals?](tcdirectionpaddescriptor/downvisuals.md)
  The visuals for the down button.
- [var hasMutuallyExclusiveInput: Bool](tcdirectionpaddescriptor/hasmutuallyexclusiveinput.md)
  A Boolean value that indicates whether the control has mutally exclusive input.
- [var highlightTime: simd_float1](tcdirectionpaddescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isDigital: Bool](tcdirectionpaddescriptor/isdigital.md)
  A Boolean value that indicates whether the control behaves as a digital button.
- [var isRadial: Bool](tcdirectionpaddescriptor/isradial.md)
  A Boolean value that indicates whether the control behaves as a swipeable radial button.
- [var leftLabel: TCControlLabel?](tcdirectionpaddescriptor/leftlabel.md)
  The label for the left button, if the control is not a composite direction pad.
- [var leftVisuals: TCControlVisuals?](tcdirectionpaddescriptor/leftvisuals.md)
  The visuals for the left button.
- [var offset: CGPoint](tcdirectionpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var rightLabel: TCControlLabel?](tcdirectionpaddescriptor/rightlabel.md)
  The label for the right button, if the control is not a composite direction pad.
- [var rightVisuals: TCControlVisuals?](tcdirectionpaddescriptor/rightvisuals.md)
  The visuals for the right button.
- [var size: CGSize](tcdirectionpaddescriptor/size.md)
  The size (width, height) of the direction pad in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcdirectionpaddescriptor/layer)*