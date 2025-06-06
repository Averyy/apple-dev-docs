# toolbar

**Framework**: UIKit  
**Kind**: property

The custom toolbar associated with the navigation controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var toolbar: UIToolbar! { get }
```

#### Discussion

This property contains a reference to the built-in toolbar managed by the navigation controller. Access to this toolbar is provided solely for clients that want to present an action sheet from the toolbar. You should not modify the [`UIToolbar`](uitoolbar.md) object directly.

Management of this toolbar’s contents is done through the custom view controllers associated with this navigation controller. For each view controller on the navigation stack, you can assign a custom set of toolbar items using the [`setToolbarItems(_:animated:)`](uiviewcontroller/settoolbaritems(_:animated:).md) method of [`UIViewController`](uiviewcontroller.md).

The visibility of this toolbar is controlled by the [`isToolbarHidden`](uinavigationcontroller/istoolbarhidden.md) property. The toolbar also obeys the [`hidesBottomBarWhenPushed`](uiviewcontroller/hidesbottombarwhenpushed.md) property of the currently visible view controller and hides and shows itself automatically as needed.

## See Also

- [func setToolbarHidden(Bool, animated: Bool)](uinavigationcontroller/settoolbarhidden(_:animated:).md)
  Changes the visibility of the navigation controller’s built-in toolbar.
- [var isToolbarHidden: Bool](uinavigationcontroller/istoolbarhidden.md)
  A Boolean indicating whether the navigation controller’s built-in toolbar is visible.
- [class let hideShowBarDuration: CGFloat](uinavigationcontroller/hideshowbarduration.md)
  A variable that specifies the duration when animating the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/toolbar)*