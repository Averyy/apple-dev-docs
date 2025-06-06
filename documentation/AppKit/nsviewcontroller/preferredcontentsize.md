# preferredContentSize

**Framework**: AppKit  
**Kind**: property

The desired size of the view controller’s view, in screen units.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var preferredContentSize: NSSize { get set }
```

#### Discussion

Set this property to express the desired size for a view controller’s view. A parent view controller can consult the value of this property when performing layout.

## See Also

- [var preferredMaximumSize: NSSize](nsviewcontroller/preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](nsviewcontroller/preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [var preferredScreenOrigin: NSPoint](nsviewcontroller/preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [func updateViewConstraints()](nsviewcontroller/updateviewconstraints.md)
  Called during Auto Layout constraint updating to enable the view controller to mediate the process.
- [func viewWillLayout()](nsviewcontroller/viewwilllayout.md)
  Called just before the [`layout()`](nsview/layout().md) method of the view controller’s view is called.
- [func viewDidLayout()](nsviewcontroller/viewdidlayout.md)
  Called immediately after the [`layout()`](nsview/layout().md) method of the view controller’s view is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredcontentsize)*