# preferredContentSizeDidChange(forChildContentContainer:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies an interested controller that the preferred content size of one of its children changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func preferredContentSizeDidChange(forChildContentContainer container: any UIContentContainer)
```

#### Discussion

UIKit calls this method on a container view controller when the [`preferredContentSize`](uicontentcontainer/preferredcontentsize.md) property of one of its child view controllers changes. Similarly, if the view controller is managed by a presentation controller, UIKit calls this method on the presentation controller to let it know of the change. The parent view controller or presentation controller can use this method to initiate layout adjustments based on the new size information.

## Parameters

- `container`: The child view controller whose preferred content size has changed.

## See Also

- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:).md)
  Returns the size of the specified child view controller’s content.
- [func systemLayoutFittingSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:).md)
  Notifies the container that a child view controller was resized using Auto Layout.
- [var preferredContentSize: CGSize](uicontentcontainer/preferredcontentsize.md)
  The preferred size for the container’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:))*