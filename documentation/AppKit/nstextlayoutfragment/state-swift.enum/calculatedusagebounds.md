# NSTextLayoutFragment.State.calculatedUsageBounds

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The layout fragment measurements are available without text line fragments.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case calculatedUsageBounds
```

```c
NSTextLayoutFragmentStateCalculatedUsageBounds
```

## See Also

### Constants that describe layout bounds
- [NSTextLayoutFragment.State.estimatedUsageBounds](./estimatedusagebounds.md)
  The text layout manager hasn’t performed a full layout yet for the region covered by this layout fragment and is returning an estimated bounds.
- [NSTextLayoutFragment.State.layoutAvailable](./layoutavailable.md)
  Measurements for the text line fragments and layout fragment are available.
- [NSTextLayoutFragment.State.none](./none.md)
  No layout information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/state-swift.enum/calculatedusagebounds)*