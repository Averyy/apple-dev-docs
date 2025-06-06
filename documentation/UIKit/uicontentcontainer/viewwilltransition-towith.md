# viewWillTransition(to:with:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies the container that the size of its view is about to change.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewWillTransition(to size: CGSize, with coordinator: any UIViewControllerTransitionCoordinator)
```

#### Discussion

UIKit calls this method before changing the size of a presented view controller’s view. You can override this method in your own objects and use it to perform additional tasks related to the size change. For example, a container view controller might use this method to override the traits of its embedded child view controllers. Use the provided `coordinator` object to animate any changes you make.

If you override this method in your custom view controllers, always call `super` at some point in your implementation so that UIKit can forward the size change message appropriately. View controllers forward the size change message to their views and child view controllers. Presentation controllers forward the size change to their presented view controller.

## Parameters

- `size`: The new size for the container’s view.
- `coordinator`: The transition coordinator object managing the size change. You can use this object to animate your changes or get information about the transition that is in progress.

## See Also

- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:).md)
  Returns the size of the specified child view controller’s content.
- [func willTransition(to: UITraitCollection, with: any UIViewControllerTransitionCoordinator)](uicontentcontainer/willtransition(to:with:).md)
  Notifies the container that its trait collection changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/viewwilltransition(to:with:))*