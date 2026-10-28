# multiple

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and dragged positions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var multiple: NSTextSelectionNavigation.Modifier { get }
```

```c
NSTextSelectionNavigationModifierMultiple
```

## Discussion

This produces an [`NSTextSelection`](../../nstextselection.md) per line.

## See Also

### Navigation modifier characteristics
- [static var extend: NSTextSelectionNavigation.Modifier](./extend.md)
  The value that indicates the framework extends the selection by not moving the initial location while in a drag selection.
- [static var visual: NSTextSelectionNavigation.Modifier](./visual.md)
  The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and drag positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/modifier/multiple)*