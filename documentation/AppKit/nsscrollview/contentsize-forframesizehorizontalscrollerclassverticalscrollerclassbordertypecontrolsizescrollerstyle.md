# contentSize(forFrameSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:)

**Framework**: AppKit  
**Kind**: method

Returns the content size calculated from the frame size and the specified specifications.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class func contentSize(forFrameSize fSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType type: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize
```

#### Return Value

The content view frame size.

#### Discussion

For an existing scroll view, you can simply use the [`contentSize`](nsscrollview/contentsize.md) property.

## Parameters

- `fSize`: The frame size in screen coordinates.
- `horizontalScrollerClass`: The class used as the horizontal scroller. A value of   specifies that no horizontal scroller is used.
- `verticalScrollerClass`: The class used as the vertical scroller. A value of   specifies that no horizontal scroller is used.
- `type`: Specifies the appearance of the style of the scroll view’s border. See   for a list of possible values.
- `controlSize`: The control size. The possible values are specified in  .   is not supported.
- `scrollerStyle`: Specifies the scroll style. See   for supported values.

## See Also

- [class func frameSize(forContentSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](nsscrollview/framesize(forcontentsize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:).md)
  Returns the frame size of a scroll view that contains a content view with the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/contentsize(forframesize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:))*