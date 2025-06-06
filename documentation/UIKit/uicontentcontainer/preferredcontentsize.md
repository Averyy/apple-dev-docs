# preferredContentSize

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The preferred size for the container’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredContentSize: CGSize { get }
```

#### Discussion

The [`UIViewController`](uiviewcontroller.md) class implements a writable version of this property.

## See Also

- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:).md)
  Returns the size of the specified child view controller’s content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:).md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [func systemLayoutFittingSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:).md)
  Notifies the container that a child view controller was resized using Auto Layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/preferredcontentsize)*