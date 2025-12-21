# preferredScrollEdgeEffectStyle

**Framework**: AppKit  
**Kind**: property

The titlebar accessory’s preferred effect for content scrolling behind it.

**Availability**:
- macOS 26.1+

## Declaration

```swift
@MainActor
var preferredScrollEdgeEffectStyle: NSScrollEdgeEffectStyle { get set }
```

#### Discussion

To allow for a soft edge on the bottom edge of a titlebar accessory:

```None
titlebarAccessoryViewController.preferredScrollEdgeEffectStyle = NSScrollEdgeEffectStyle.softStyle;
```

## See Also

- [class NSScrollEdgeEffectStyle](nsscrolledgeeffectstyle.md)
  Styles for a scroll view’s edge effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/preferredscrolledgeeffectstyle)*