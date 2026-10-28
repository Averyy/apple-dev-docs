# systemLayoutFittingSizeDidChange(forChildContentContainer:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the container that a child view controller was resized using Auto Layout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func systemLayoutFittingSizeDidChange(forChildContentContainer container: any UIContentContainer)
```

```objc
- (void) systemLayoutFittingSizeDidChangeForChildContentContainer:(id<UIContentContainer>) container;
```

## Discussion

This method is called when a view controller that doesn’t use Auto Layout has a child view controller that uses Auto Layout and the child view controller is resized. When the child view controller responds to the [`systemLayoutSizeFitting(_:)`](../uiview/systemlayoutsizefitting%28_%29.md) method, the [`systemLayoutFittingSizeDidChange(forChildContentContainer:)`](./systemlayoutfittingsizedidchange%28forchildcontentcontainer%29.md) method is sent to the parent view controller.

## Parameters

- `container`: The child view controller that received the resizing message.

## See Also

### Responding to changes in child view controllers
- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](./size%28forchildcontentcontainer,withparentcontainersize%29.md)
  Returns the size of the specified child view controller’s content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](./preferredcontentsizedidchange%28forchildcontentcontainer%29.md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [var preferredContentSize: CGSize](./preferredcontentsize.md)
  The preferred size for the container’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:))*