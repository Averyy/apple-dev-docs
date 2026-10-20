# toolbar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The custom toolbar associated with the navigation controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var toolbar: UIToolbar! { get }
```

```objc
@property (nonatomic, readonly, null_resettable) UIToolbar * toolbar;
```

#### Discussion

This property contains a reference to the built-in toolbar managed by the navigation controller. Access to this toolbar is provided solely for clients that want to present an action sheet from the toolbar. You should not modify the [`UIToolbar`](../uitoolbar.md) object directly.

Management of this toolbar’s contents is done through the custom view controllers associated with this navigation controller. For each view controller on the navigation stack, you can assign a custom set of toolbar items using the [`setToolbarItems(_:animated:)`](../uiviewcontroller/settoolbaritems%28_,animated%29.md) method of [`UIViewController`](../uiviewcontroller.md).

The visibility of this toolbar is controlled by the [`isToolbarHidden`](./istoolbarhidden.md) property. The toolbar also obeys the [`hidesBottomBarWhenPushed`](../uiviewcontroller/hidesbottombarwhenpushed.md) property of the currently visible view controller and hides and shows itself automatically as needed.

## See Also

### Configuring custom toolbars
- [func setToolbarHidden(Bool, animated: Bool)](./settoolbarhidden%28_,animated%29.md)
  Changes the visibility of the navigation controller’s built-in toolbar.
- [var isToolbarHidden: Bool](./istoolbarhidden.md)
  A Boolean indicating whether the navigation controller’s built-in toolbar is visible.
- [class let hideShowBarDuration: CGFloat](./hideshowbarduration.md)
  A variable that specifies the duration when animating the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/toolbar)*