# delegate

**Framework**: UIKit  
**Kind**: property

The delegate object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPageViewControllerDelegate)? { get set }
```

#### Discussion

Methods of the delegate are called in response to gesture-based navigation and orientation changes.

## See Also

- [protocol UIPageViewControllerDelegate](uipageviewcontrollerdelegate.md)
  The delegate of a page view controller must adopt the [`UIPageViewControllerDelegate`](uipageviewcontrollerdelegate.md) protocol. These methods allow the delegate to receive a notification when the device orientation changes and when the user navigates to a new page. For page-curl style transitions, the delegate can provide a different spine location in response to a change in the interface orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/delegate)*