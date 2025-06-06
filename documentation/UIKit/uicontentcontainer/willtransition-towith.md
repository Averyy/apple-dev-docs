# willTransition(to:with:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies the container that its trait collection changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func willTransition(to newCollection: UITraitCollection, with coordinator: any UIViewControllerTransitionCoordinator)
```

#### Discussion

UIKit calls this method before changing the current object’s traits and before calling the [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) method of any affected views and view controllers. Implementors of this method can use it to adapt the interface based on the values in the `newCollection` parameter. A common use of this method is to make changes to the high-level presentation style when the current size class changes. For example, a container view controller that manages multiple child view controllers might change the number of child view controllers it displays onscreen when the size class changes. A standard view controller might use this method to change the constraints on the views it manages. Use the provided `coordinator` object to animate any changes you make.

If you override this method in your own objects, always call `super` at some point in your implementation so that UIKit can forward the trait changes to the associated presentation controller and to any child view controllers. View controllers forward the trait change message to their child view controllers. Presentation controllers forward the trait change to their presented view controller.

## Parameters

- `newCollection`: The traits to be applied to the container.
- `coordinator`: The transition coordinator object managing the trait change. You can use this object to animate any changes or to get information about the transition that is in progress.

## See Also

- [func traitCollectionDidChange(UITraitCollection?)](uitraitenvironment/traitcollectiondidchange(_:).md)
  Reports changes in the iOS interface environment.
- [func viewWillTransition(to: CGSize, with: any UIViewControllerTransitionCoordinator)](uicontentcontainer/viewwilltransition(to:with:).md)
  Notifies the container that the size of its view is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/willtransition(to:with:))*