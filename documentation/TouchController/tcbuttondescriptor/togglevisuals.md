# toggleVisuals

**Framework**: Touch Controller  
**Kind**: property

The visuals for the button when it is toggled on.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var toggleVisuals: TCControlVisuals? { get set }
```

#### Discussion

This value is only used when the button is a toggle, and can be `nil`.

## See Also

- [var anchor: TCTransformAnchor](tcbuttondescriptor/anchor.md)
  The anchor point that the button’s offset is relative to.
- [var colliderType: TCColliderType](tcbuttondescriptor/collidertype.md)
  The type of collider to use for the button.
- [var highlightTime: simd_float1](tcbuttondescriptor/highlighttime.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isToggle: Bool](tcbuttondescriptor/istoggle.md)
  Whether the button is a toggle button.
- [var label: TCControlLabel](tcbuttondescriptor/label.md)
  The label you associate with the button.
- [var layer: simd_int1](tcbuttondescriptor/layer.md)
  The layer of the button, used for z-sorting.
- [var offset: CGPoint](tcbuttondescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcbuttondescriptor/size.md)
  The size (width, height) of the button in points.
- [var visuals: TCControlVisuals?](tcbuttondescriptor/visuals.md)
  The visuals for the button in its normal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcbuttondescriptor/togglevisuals)*