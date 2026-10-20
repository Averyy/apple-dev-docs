# NSTextLayoutFragment.State.layoutAvailable

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Measurements for the text line fragments and layout fragment are available.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case layoutAvailable
```

```c
NSTextLayoutFragmentStateLayoutAvailable
```

## See Also

### Constants that describe layout bounds
- [NSTextLayoutFragment.State.calculatedUsageBounds](./calculatedusagebounds.md)
  The layout fragment measurements are available without text line fragments.
- [NSTextLayoutFragment.State.estimatedUsageBounds](./estimatedusagebounds.md)
  The text layout manager hasn’t performed a full layout yet for the region covered by this layout fragment and is returning an estimated bounds.
- [NSTextLayoutFragment.State.none](./none.md)
  No layout information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/state-swift.enum/layoutavailable)*