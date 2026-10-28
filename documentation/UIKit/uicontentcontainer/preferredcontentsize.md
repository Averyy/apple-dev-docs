# preferredContentSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The preferred size for the container’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var preferredContentSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize preferredContentSize;
```

## Discussion

The [`UIViewController`](../uiviewcontroller.md) class implements a writable version of this property.

## See Also

### Responding to changes in child view controllers
- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](./size%28forchildcontentcontainer,withparentcontainersize%29.md)
  Returns the size of the specified child view controller’s content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](./preferredcontentsizedidchange%28forchildcontentcontainer%29.md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [func systemLayoutFittingSizeDidChange(forChildContentContainer: any UIContentContainer)](./systemlayoutfittingsizedidchange%28forchildcontentcontainer%29.md)
  Notifies the container that a child view controller was resized using Auto Layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer/preferredcontentsize)*