# contentSize(forFrameSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the content size calculated from the frame size and the specified specifications.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func contentSize(forFrameSize fSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType type: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize
```

```objc
+ (NSSize) contentSizeForFrameSize:(NSSize) fSize horizontalScrollerClass:(Class) horizontalScrollerClass verticalScrollerClass:(Class) verticalScrollerClass borderType:(NSBorderType) type controlSize:(NSControlSize) controlSize scrollerStyle:(NSScrollerStyle) scrollerStyle;
```

## Return Value

The content view frame size.

## Discussion

For an existing scroll view, you can simply use the [`contentSize`](./contentsize.md) property.

## Parameters

- `fSize`: The frame size in screen coordinates.
- `horizontalScrollerClass`: The class used as the horizontal scroller. A value of `nil` specifies that no horizontal scroller is used.
- `verticalScrollerClass`: The class used as the vertical scroller. A value of `nil` specifies that no horizontal scroller is used.
- `type`: Specifies the appearance of the style of the scroll view’s border. See [`NSBorderType`](../nsbordertype.md) for a list of possible values.
- `controlSize`: The control size. The possible values are specified in [`NSControl.ControlSize`](../nscontrol/controlsize-swift.enum.md). [`NSMiniControlSize`](../nsminicontrolsize.md) is not supported.
- `scrollerStyle`: Specifies the scroll style. See [`NSScroller.Style`](../nsscroller/style.md) for supported values.

## See Also

### Calculating Layout
- [class func frameSize(forContentSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](./framesize%28forcontentsize,horizontalscrollerclass,verticalscrollerclass,bordertype,controlsize,scrollerstyle%29.md)
  Returns the frame size of a scroll view that contains a content view with the specified size.
- [+ frameSizeForContentSize:hasHorizontalScroller:hasVerticalScroller:borderType:](./framesizeforcontentsize_hashorizontalscroller_hasverticalscroller_bordertype_.md)
  Returns the frame size of an scroll view that contains a content view with the specified size.
- [+ contentSizeForFrameSize:hasHorizontalScroller:hasVerticalScroller:borderType:](./contentsizeforframesize_hashorizontalscroller_hasverticalscroller_bordertype_.md)
  Returns the content size calculated from the frame size and the specified specifications.
### Related Documentation
- [+ scrollerWidth](../nsscroller/scrollerwidth.md)
  Returns the width for scrollers of the receiving class, assuming a control size [`NSRegularControlSize`](../nsregularcontrolsize.md), and a scroller style of [`NSScrollerStyleLegacy`](../nsscroller/style/legacy.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/contentsize(forframesize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:))*