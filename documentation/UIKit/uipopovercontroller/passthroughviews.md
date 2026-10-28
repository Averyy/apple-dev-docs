# passthroughViews

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of views that the user can interact with while the popover is visible.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
var passthroughViews: [UIView]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<__kindof UIView *> * passthroughViews;
```

## Discussion

When a popover is active, interactions with other views are normally disabled until the popover is dismissed. Assigning an array of views to this property allows taps outside of the popover to be handled by the corresponding views.

## See Also

### Configuring the popover content
- [var contentViewController: UIViewController](./contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [func setContentView(UIViewController, animated: Bool)](./setcontentview%28_,animated%29.md)
  Sets the view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](./contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](./setcontentsize%28_,animated%29.md)
  Changes the size of the popover’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/passthroughviews)*