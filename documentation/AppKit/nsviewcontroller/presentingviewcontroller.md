# presentingViewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view controller that presented the view controller or that presented its farthest ancestor view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
unowned(unsafe) var presentingViewController: NSViewController? { get }
```

```objc
@property (assign, readonly, nullable) NSViewController * presentingViewController;
```

#### Discussion

The *presenting view controller* is the one that is ultimately responsible for presenting the view controller whose [`presentingViewController`](./presentingviewcontroller.md) property you are accessing.

## See Also

### Getting Related View Controllers
- [var parent: NSViewController?](./parent.md)
  The immediate ancestor view controller of the view controller.
- [var presentedViewControllers: [NSViewController]?](./presentedviewcontrollers.md)
  The view controllers, if any, that are currently presented by the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentingviewcontroller)*