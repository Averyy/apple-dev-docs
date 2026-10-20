# multiple

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and dragged positions.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static var multiple: NSTextSelectionNavigation.Modifier { get }
```

```c
NSTextSelectionNavigationModifierMultiple
```

#### Discussion

This produces an [`NSTextSelection`](../../nstextselection.md) per line.

## See Also

### Navigation modifier characteristics
- [static var extend: NSTextSelectionNavigation.Modifier](./extend.md)
  The value that indicates the framework extends the selection by not moving the initial location while in a drag selection.
- [static var visual: NSTextSelectionNavigation.Modifier](./visual.md)
  The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and drag positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/modifier/multiple)*