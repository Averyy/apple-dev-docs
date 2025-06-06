# Positioning content relative to the safe area

**Framework**: UIKit

Position views so that they aren’t obstructed by other content.

#### Overview

Safe areas help you place your views within the visible portion of the overall interface. UIKit-defined view controllers may position special views on top of your content. For example, a navigation controller displays a navigation bar on top of the underlying view controller’s content. Even when such views are partially transparent, they still occlude the content that’s underneath them. In tvOS, the safe area also includes the screen’s overscan insets, which represent the area covered by the screen’s bezel.

Use safe areas as an aid to laying out your content. Each view has its own layout guide (accessible from the [`safeAreaLayoutGuide`](uiview/safearealayoutguide.md) property) that you can use to create constraints for items inside the view. If you aren’t using Auto Layout to position your views, you can obtain the raw inset values from the view’s [`safeAreaInsets`](uiview/safeareainsets.md) property.

The following image shows two different devices with a view of the Calendar app and the safe area associated with each one.

![Safe areas in the Calendar app on two different iPhones.](https://docs-assets.developer.apple.com/published/ffae6eeb748a98b98bf68da66fa244db/media-2936293%402x.png)

##### Extend the Safe Area to Include Custom Views

Your container view controller can display its own content views over the views of an embedded child view controller. In this situation, update the child view controller’s safe area to exclude the areas covered by the container view controller’s content views. UIKit container view controllers already adjust the safe area of their child view controllers to account for content views. For example, navigation controllers extend the safe area of their child view controllers to account for the navigation bar.

To extend the safe area of an embedded child view controller, modify its [`additionalSafeAreaInsets`](uiviewcontroller/additionalsafeareainsets.md) property. Suppose you define a container view controller that displays custom views along the bottom and right edges of the screen, as shown in the following image. Because the child view controller’s content is underneath the custom views, you must extend the bottom and right insets of the child view controller’s safe area to account for those views.

![Adjusting the safe area to account for custom views.](https://docs-assets.developer.apple.com/published/07e0575dc30eaa858523501b9f19ad09/media-2927047%402x.png)

The following code shows the [`viewDidAppear(_:)`](uiviewcontroller/viewdidappear(_:).md) method of the container view controller that extends the safe area of its child view controller to account for the custom views, as shown in the image. Make your modifications in this method because the safe area insets for a view aren’t accurate until the view is added to a view hierarchy.

```swift
override func viewDidAppear(_ animated: Bool) {
   var newSafeArea = UIEdgeInsets()
   // Adjust the safe area to accommodate 
   //  the width of the side view.
   if let sideViewWidth = sideView?.bounds.size.width {
      newSafeArea.right += sideViewWidth
   }
   // Adjust the safe area to accommodate 
   //  the height of the bottom view.
   if let bottomViewHeight = bottomView?.bounds.size.height {
      newSafeArea.bottom += bottomViewHeight
   }
   // Adjust the safe area insets of the 
   //  embedded child view controller.
   let child = self.childViewControllers[0]
   child.additionalSafeAreaInsets = newSafeArea
}
```

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [class NSLayoutConstraint](nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
- [protocol UILayoutSupport](uilayoutsupport.md)
  A set of methods that provide layout support and access to layout anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/positioning-content-relative-to-the-safe-area)*