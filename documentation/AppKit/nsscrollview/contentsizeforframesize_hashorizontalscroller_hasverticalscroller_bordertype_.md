# contentSizeForFrameSize:hasHorizontalScroller:hasVerticalScroller:borderType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the content size calculated from the frame size and the specified specifications.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`contentSize(forFrameSize:horizontalScrollerClass:verticalScrollerClass:borderType:controlSize:scrollerStyle:)`](./contentsize%28forframesize,horizontalscrollerclass,verticalscrollerclass,bordertype,controlsize,scrollerstyle%29.md) instead.

## Declaration

```objc
+ (NSSize) contentSizeForFrameSize:(NSSize) fSize hasHorizontalScroller:(BOOL) hFlag hasVerticalScroller:(BOOL) vFlag borderType:(NSBorderType) type;
```

#### Return Value

The content view frame size.

#### Discussion

For an existing scroll view, you can simply use the [`contentSize`](./contentsize.md) property.

## Parameters

- `fSize`: The frame size in the screen coordinate system
- `hFlag`: A Boolean specifying that a horizontal scroller should be included.
- `vFlag`: A Boolean specifying that a vertical scroller should be included.
- `type`: Specifies the appearance of the style of the scroll view’s border. See [`NSBorderType`](../nsbordertype.md) for a list of possible values.

## See Also

### Calculating Layout
- [class func frameSize(forContentSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](./framesize%28forcontentsize,horizontalscrollerclass,verticalscrollerclass,bordertype,controlsize,scrollerstyle%29.md)
  Returns the frame size of a scroll view that contains a content view with the specified size.
- [class func contentSize(forFrameSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](./contentsize%28forframesize,horizontalscrollerclass,verticalscrollerclass,bordertype,controlsize,scrollerstyle%29.md)
  Returns the content size calculated from the frame size and the specified specifications.
- [+ frameSizeForContentSize:hasHorizontalScroller:hasVerticalScroller:borderType:](./framesizeforcontentsize_hashorizontalscroller_hasverticalscroller_bordertype_.md)
  Returns the frame size of an scroll view that contains a content view with the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/contentsizeforframesize:hashorizontalscroller:hasverticalscroller:bordertype:)*