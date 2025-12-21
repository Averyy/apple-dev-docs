# containerViewDidLayoutSubviews()

**Framework**: UIKit  
**Kind**: method

Notifies the presentation controller when layout ends on the views of the container view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func containerViewDidLayoutSubviews()
```

#### Discussion

UIKit calls this method after adjusting the layout of the views in the container view. Use this method to make any additional changes to the view hierarchy.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this presentation controller’s `traitCollection` and the `traitCollection` of its [`containerView`](uipresentationcontroller/containerview.md). For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## See Also

- [func containerViewWillLayoutSubviews()](uipresentationcontroller/containerviewwilllayoutsubviews.md)
  Notifies the presentation controller that layout is about to begin on the views of the container view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/containerviewdidlayoutsubviews())*