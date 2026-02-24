# frameSize(forContentSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:)

**Framework**: AppKit  
**Kind**: method

Returns the frame size of a scroll view that contains a content view with the specified size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func frameSize(forContentSize cSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType type: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize
```

#### Return Value

The size of the frame for the specified `contentSize`.

#### Discussion

For an existing scroll view, you can simply use the `frame` method and extract its size.

## Parameters

- `cSize`: The content size.
- `horizontalScrollerClass`: The class used as the horizontal scroller. A value of `nil` specifies that no horizontal scroller is used.
- `verticalScrollerClass`: The class used as the vertical scroller. A value of `nil` specifies that no horizontal scroller is used.
- `type`: Specifies the appearance of the style of the scroll view’s border. See [`NSBorderType`](nsbordertype.md) for a list of possible values.
- `controlSize`: The control size. The possible values are specified in [`NSControl.ControlSize`](nscontrol/controlsize-swift.enum.md). [`NSMiniControlSize`](nsminicontrolsize.md) is not supported.
- `scrollerStyle`: Specifies the scroll style. See [`NSScroller.Style`](nsscroller/style.md) for supported values.

## See Also

- [Scroll View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSScrollViewGuide/Articles/Introduction.html#//apple_ref/doc/uid/TP40003221)
- [class func contentSize(forFrameSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](nsscrollview/contentsize(forframesize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:).md)
  Returns the content size calculated from the frame size and the specified specifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/framesize(forcontentsize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:))*