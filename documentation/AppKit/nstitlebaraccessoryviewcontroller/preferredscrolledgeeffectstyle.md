# preferredScrollEdgeEffectStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The titlebar accessory’s preferred effect for content scrolling behind it.

**Availability**:
- macOS 26.1+

## Declaration

```swift
var preferredScrollEdgeEffectStyle: NSScrollEdgeEffectStyle { get set }
```

```objc
@property (strong) NSScrollEdgeEffectStyle * preferredScrollEdgeEffectStyle;
```

## Discussion

To allow for a soft edge on the bottom edge of a titlebar accessory:

```
titlebarAccessoryViewController.preferredScrollEdgeEffectStyle = NSScrollEdgeEffectStyle.softStyle;
```

## See Also

### Configuring the scroll edge effect
- [class NSScrollEdgeEffectStyle](../nsscrolledgeeffectstyle.md)
  Styles for a scroll view’s edge effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/preferredscrolledgeeffectstyle)*