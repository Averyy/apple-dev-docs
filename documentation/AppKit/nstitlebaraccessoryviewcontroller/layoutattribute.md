# layoutAttribute

**Framework**: AppKit  
**Kind**: property

The location of the accessory view, in relation to the window’s title bar.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var layoutAttribute: NSLayoutConstraint.Attribute { get set }
```

#### Discussion

The default value of this property is [`NSLayoutConstraint.Attribute.bottom`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/bottom), which means that the accessory view should display below the title bar. You can also set this property to [`NSLayoutConstraint.Attribute.right`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/right) or (in apps linked on macOS 10.11 or later) [`NSLayoutConstraint.Attribute.left`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/left). All other values are invalid and will cause an assertion to be raised.

> **Note**:  In an app linked on macOS 10.11 or later, setting [`layoutAttribute`](nstitlebaraccessoryviewcontroller/layoutattribute.md) to [`NSLayoutConstraint.Attribute.right`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/right) does not right indent toolbar items unless the window’s [`titleVisibility`](nswindow/titlevisibility-swift.property.md) property is equal to [`NSWindow.TitleVisibility.hidden`](nswindow/titlevisibility-swift.enum/hidden.md).

## See Also

- [var fullScreenMinHeight: CGFloat](nstitlebaraccessoryviewcontroller/fullscreenminheight.md)
  The visual minimum height of an accessory view that displays below the title bar when the window is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/layoutattribute)*