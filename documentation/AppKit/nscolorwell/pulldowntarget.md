# pulldownTarget

**Framework**: AppKit  
**Kind**: property

The target object that defines the action you want to perform when someone interacts with the color well.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
weak var pulldownTarget: AnyObject? { get set }
```

#### Discussion

Specify a custom action method to replace the system popover and color picker. For a color well with the [`NSColorWell.Style.minimal`](nscolorwell/style/minimal.md) or [`NSColorWell.Style.expanded`](nscolorwell/style/expanded.md) style, clicks in the color area normally display a popover with the system color picker.  If you specify a value for this property and the [`pulldownAction`](nscolorwell/pulldownaction.md) property, clicks in the color area execute your custom action method instead.

## See Also

- [var pulldownAction: Selector?](nscolorwell/pulldownaction.md)
  The action to perform when someone clicks in the color area of the color well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/pulldowntarget)*