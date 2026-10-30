# frameSize(forContentSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the frame size of a scroll view that contains a content view with the specified size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func frameSize(forContentSize cSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType type: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize
```

```objc
+ (NSSize) frameSizeForContentSize:(NSSize) cSize horizontalScrollerClass:(Class) horizontalScrollerClass verticalScrollerClass:(Class) verticalScrollerClass borderType:(NSBorderType) type controlSize:(NSControlSize) controlSize scrollerStyle:(NSScrollerStyle) scrollerStyle;
```

## Return Value

The size of the frame for the specified `contentSize`.

## Discussion

For an existing scroll view, you can simply use the `frame` method and extract its size.

## Parameters

- `cSize`: The content size.
- `horizontalScrollerClass`: The class used as the horizontal scroller. A value of `nil` specifies that no horizontal scroller is used.
- `verticalScrollerClass`: The class used as the vertical scroller. A value of `nil` specifies that no horizontal scroller is used.
- `type`: Specifies the appearance of the style of the scroll view’s border. See [`NSBorderType`](../nsbordertype.md) for a list of possible values.
- `controlSize`: The control size. The possible values are specified in [`NSControl.ControlSize`](../nscontrol/controlsize-swift.enum.md). [`NSMiniControlSize`](../nsminicontrolsize.md) is not supported.
- `scrollerStyle`: Specifies the scroll style. See [`NSScroller.Style`](../nsscroller/style.md) for supported values.

## See Also

### Related Documentation
- [Scroll View Programming Guide for Mac](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSScrollViewGuide/Articles/Introduction.html#//apple_ref/doc/uid/TP40003221)
- [+ scrollerWidth](../nsscroller/scrollerwidth.md)
  Returns the width for scrollers of the receiving class, assuming a control size [`NSRegularControlSize`](../nsregularcontrolsize.md), and a scroller style of [`NSScrollerStyleLegacy`](../nsscroller/style/legacy.md).
### Calculating layout
- [class func contentSize(forFrameSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](./contentsize%28forframesize,horizontalscrollerclass,verticalscrollerclass,bordertype,controlsize,scrollerstyle%29.md)
  Returns the content size calculated from the frame size and the specified specifications.
- [+ frameSizeForContentSize:hasHorizontalScroller:hasVerticalScroller:borderType:](./framesizeforcontentsize_hashorizontalscroller_hasverticalscroller_bordertype_.md)
  Returns the frame size of an scroll view that contains a content view with the specified size.
- [+ contentSizeForFrameSize:hasHorizontalScroller:hasVerticalScroller:borderType:](./contentsizeforframesize_hashorizontalscroller_hasverticalscroller_bordertype_.md)
  Returns the content size calculated from the frame size and the specified specifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/framesize(forcontentsize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:))*