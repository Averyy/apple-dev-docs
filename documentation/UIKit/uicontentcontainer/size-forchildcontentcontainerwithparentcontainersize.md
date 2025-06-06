# size(forChildContentContainer:withParentContainerSize:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the size of the specified child view controller’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func size(forChildContentContainer container: any UIContentContainer, withParentContainerSize parentSize: CGSize) -> CGSize
```

#### Return Value

The size to apply to the child view controller.

#### Discussion

Container view controllers use this method to return the sizes for their child view controllers. UIKit calls the method as part of the default implementation of the [`viewWillTransition(to:with:)`](uicontentcontainer/viewwilltransition(to:with:).md) method for view controllers. It calls the method once for each child view controller embedded in the view controller. If you’re implementing a custom container view controller, you should override this method and use it to return the sizes of the contained children.

View controllers and presentation controllers return the value in `parentSize` by default.

## Parameters

- `container`: The child view controller.
- `parentSize`: The size of the parent view controller.

## See Also

- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:).md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [func systemLayoutFittingSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:).md)
  Notifies the container that a child view controller was resized using Auto Layout.
- [var preferredContentSize: CGSize](uicontentcontainer/preferredcontentsize.md)
  The preferred size for the container’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:))*