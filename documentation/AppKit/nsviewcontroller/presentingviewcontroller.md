# presentingViewController

**Framework**: AppKit  
**Kind**: property

The view controller that presented the view controller or that presented its farthest ancestor view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
unowned(unsafe) var presentingViewController: NSViewController? { get }
```

#### Discussion

The  is the one that is ultimately responsible for presenting the view controller whose [`presentingViewController`](nsviewcontroller/presentingviewcontroller.md) property you are accessing.

## See Also

- [var parent: NSViewController?](nsviewcontroller/parent.md)
  The immediate ancestor view controller of the view controller.
- [var presentedViewControllers: [NSViewController]?](nsviewcontroller/presentedviewcontrollers.md)
  The view controllers, if any, that are currently presented by the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentingviewcontroller)*