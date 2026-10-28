# pulldownTarget

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The target object that defines the action you want to perform when someone interacts with the color well.

**Availability**:
- macOS 13.0+

## Declaration

```swift
weak var pulldownTarget: AnyObject? { get set }
```

```objc
@property (weak, nullable) id pulldownTarget;
```

## Discussion

Specify a custom action method to replace the system popover and color picker. For a color well with the [`NSColorWell.Style.minimal`](./style/minimal.md) or [`NSColorWell.Style.expanded`](./style/expanded.md) style, clicks in the color area normally display a popover with the system color picker.  If you specify a value for this property and the [`pulldownAction`](./pulldownaction.md) property, clicks in the color area execute your custom action method instead.

## See Also

### Customizing the color selection behavior
- [var pulldownAction: Selector?](./pulldownaction.md)
  The action to perform when someone clicks in the color area of the color well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/pulldowntarget)*