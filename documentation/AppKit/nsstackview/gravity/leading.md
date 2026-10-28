# leading

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var leading: NSStackView.Gravity { get }
```

```c
NSStackViewGravityLeading
```

## Discussion

For a left to right layout direction, the leading gravity area is on the left. Use only when the value of the [`orientation`](../orientation.md) property is [`NSUserInterfaceLayoutOrientation.horizontal`](../../nsuserinterfacelayoutorientation/horizontal.md).

## See Also

### Constants
- [NSStackView.Gravity.top](./top.md)
  The topmost gravity area in a vertically oriented stack view.
- [NSStackView.Gravity.center](./center.md)
  The center gravity area, regardless of stack view layout direction or user interface language.
- [NSStackView.Gravity.bottom](./bottom.md)
  The bottommost gravity area in a vertically oriented stack view.
- [static var trailing: NSStackView.Gravity](./trailing.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/gravity/leading)*