# systemLayoutFittingSizeDidChange(forChildContentContainer:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies the container that a child view controller was resized using Auto Layout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func systemLayoutFittingSizeDidChange(forChildContentContainer container: any UIContentContainer)
```

#### Discussion

This method is called when a view controller that doesn’t use Auto Layout has a child view controller that uses Auto Layout and the child view controller is resized. When the child view controller responds to the [`systemLayoutSizeFitting(_:)`](uiview/systemlayoutsizefitting(_:).md) method, the [`systemLayoutFittingSizeDidChange(forChildContentContainer:)`](uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:).md) method is sent to the parent view controller.

## Parameters

- `container`: The child view controller that received the resizing message.

## See Also

- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:).md)
  Returns the size of the specified child view controller’s content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:).md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [var preferredContentSize: CGSize](uicontentcontainer/preferredcontentsize.md)
  The preferred size for the container’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:))*