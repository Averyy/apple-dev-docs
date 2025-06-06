# NSTextFinderBarContainer

**Framework**: AppKit  
**Kind**: protocol

A protocol that provides a container in which the find bar is displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextFinderBarContainer : NSObjectProtocol
```

#### Overview

To display the find bar, a container for the find bar must be specified. You specify a find bar container using the [`findBarContainer`](nstextfinder/findbarcontainer.md) of the [`NSTextFinder`](nstextfinder.md) class.

See [`NSTextFinder`](nstextfinder.md) for more information.

## Topics

### Find Bar View
- [var findBarView: NSView?](nstextfinderbarcontainer/findbarview.md)
  The view assigned by the text bar as the find bar view for the container.
- [func contentView() -> NSView?](nstextfinderbarcontainer/contentview.md)
  A view hierarchy that contains all the views which display the contents being searched.
- [var isFindBarVisible: Bool](nstextfinderbarcontainer/isfindbarvisible.md)
  Returns whether the container should display its find bar.
### Find Bar Height
- [func findBarViewDidChangeHeight()](nstextfinderbarcontainer/findbarviewdidchangeheight.md)
  Notifies the find bar container that the find bar has changed its height.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSScrollView](nsscrollview.md)

## See Also

- [class NSTextFinder](nstextfinder.md)
  An optional search-and-replace find interface inside a view, usually a scroll view.
- [protocol NSTextFinderClient](nstextfinderclient.md)
  A set of methods implemented by objects that support searching using the [`NSTextFinder`](nstextfinder.md) class and the in-window text find bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderbarcontainer)*