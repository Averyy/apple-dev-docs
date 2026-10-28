# presentedViewControllers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view controllers, if any, that are currently presented by the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var presentedViewControllers: [NSViewController]? { get }
```

```objc
@property (readonly, nullable) NSArray<__kindof NSViewController *> * presentedViewControllers;
```

## Discussion

There is a one-to-many relationship between the view controller whose [`presentedViewControllers`](./presentedviewcontrollers.md) property you are accessing, and the view controllers it is currently presenting.

## See Also

### Getting Related View Controllers
- [var parent: NSViewController?](./parent.md)
  The immediate ancestor view controller of the view controller.
- [var presentingViewController: NSViewController?](./presentingviewcontroller.md)
  The view controller that presented the view controller or that presented its farthest ancestor view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentedviewcontrollers)*