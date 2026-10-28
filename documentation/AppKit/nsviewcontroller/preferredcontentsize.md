# preferredContentSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The desired size of the view controller’s view, in screen units.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var preferredContentSize: NSSize { get set }
```

```objc
@property NSSize preferredContentSize;
```

## Discussion

Set this property to express the desired size for a view controller’s view. A parent view controller can consult the value of this property when performing layout.

## See Also

### Related Documentation
- [var preferredMaximumSize: NSSize](./preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](./preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [var preferredScreenOrigin: NSPoint](./preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
### Managing View Layout
- [func updateViewConstraints()](./updateviewconstraints%28%29.md)
  Called during Auto Layout constraint updating to enable the view controller to mediate the process.
- [func viewWillLayout()](./viewwilllayout%28%29.md)
  Called just before the [`layout()`](../nsview/layout%28%29.md) method of the view controller’s view is called.
- [func viewDidLayout()](./viewdidlayout%28%29.md)
  Called immediately after the [`layout()`](../nsview/layout%28%29.md) method of the view controller’s view is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredcontentsize)*