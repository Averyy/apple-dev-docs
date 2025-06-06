# parent

**Framework**: AppKit  
**Kind**: property

The immediate ancestor view controller of the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var parent: NSViewController? { get }
```

#### Discussion

The value of this property is `nil` if the view controller has no parent view controller, such as if the view controller is a window’s content view controller.

## See Also

- [var presentedViewControllers: [NSViewController]?](nsviewcontroller/presentedviewcontrollers.md)
  The view controllers, if any, that are currently presented by the view controller.
- [var presentingViewController: NSViewController?](nsviewcontroller/presentingviewcontroller.md)
  The view controller that presented the view controller or that presented its farthest ancestor view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/parent)*