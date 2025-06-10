# NSTextLayoutFragment.State

**Framework**: AppKit  
**Kind**: enum

Values that describe the possible layout states.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum State
```

## Topics

### Constants that describe layout bounds
- [NSTextLayoutFragment.State.calculatedUsageBounds](nstextlayoutfragment/state-swift.enum/calculatedusagebounds.md)
  The layout fragment measurements are available without text line fragments.
- [NSTextLayoutFragment.State.estimatedUsageBounds](nstextlayoutfragment/state-swift.enum/estimatedusagebounds.md)
  The text layout manager hasn’t performed a full layout yet for the region covered by this layout fragment and is returning an estimated bounds.
- [NSTextLayoutFragment.State.layoutAvailable](nstextlayoutfragment/state-swift.enum/layoutavailable.md)
  Measurements for the text line fragments and layout fragment are available.
- [NSTextLayoutFragment.State.none](nstextlayoutfragment/state-swift.enum/none.md)
  No layout information is available.
### Initializers
- [init?(rawValue: UInt)](nstextlayoutfragment/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: NSTextLayoutFragment.State](nstextlayoutfragment/state-swift.property.md)
  The layout information state.
- [var rangeInElement: NSTextRange](nstextlayoutfragment/rangeinelement.md)
  The range inside the text element relative to the document origin.
- [var textElement: NSTextElement?](nstextlayoutfragment/textelement.md)
  The parent text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/state-swift.enum)*