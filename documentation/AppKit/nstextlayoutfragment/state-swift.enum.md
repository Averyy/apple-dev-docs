# NSTextLayoutFragment.State

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe the possible layout states.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum State
```

```c
enum NSTextLayoutFragmentState : NSUInteger;
```

## Topics

### Constants that describe layout bounds
- [NSTextLayoutFragment.State.calculatedUsageBounds](./state-swift.enum/calculatedusagebounds.md)
  The layout fragment measurements are available without text line fragments.
- [NSTextLayoutFragment.State.estimatedUsageBounds](./state-swift.enum/estimatedusagebounds.md)
  The text layout manager hasn’t performed a full layout yet for the region covered by this layout fragment and is returning an estimated bounds.
- [NSTextLayoutFragment.State.layoutAvailable](./state-swift.enum/layoutavailable.md)
  Measurements for the text line fragments and layout fragment are available.
- [NSTextLayoutFragment.State.none](./state-swift.enum/none.md)
  No layout information is available.
### Initializers
- [init?(rawValue: UInt)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting element information
- [var state: NSTextLayoutFragment.State](./state-swift.property.md)
  The layout information state.
- [var rangeInElement: NSTextRange](./rangeinelement.md)
  The range inside the text element relative to the document origin.
- [var textElement: NSTextElement?](./textelement.md)
  The parent text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/state-swift.enum)*