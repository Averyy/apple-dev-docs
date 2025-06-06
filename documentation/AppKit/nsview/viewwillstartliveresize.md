# viewWillStartLiveResize()

**Framework**: AppKit  
**Kind**: method

Informs the view of the start of a live resize—the user has started resizing the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func viewWillStartLiveResize()
```

#### Discussion

In the simple case, a view is sent [`viewWillStartLiveResize()`](nsview/viewwillstartliveresize().md) before the first resize operation on the containing window and [`viewDidEndLiveResize()`](nsview/viewdidendliveresize().md) after the last resize operation. A view that is repeatedly added and removed from a window during live resize will receive only one [`viewWillStartLiveResize()`](nsview/viewwillstartliveresize().md) (on the first time it is added to the window) and one [`viewDidEndLiveResize()`](nsview/viewdidendliveresize().md) (when the window has completed the live resize operation). This allows a superview such as [`NSBrowser`](nsbrowser.md) object to add and remove its `NSMatrix` subviews during live resize without the [`NSMatrix`](nsmatrix.md) object receiving multiple calls to these methods.

A view might allocate data structures to cache-drawing information in [`viewWillStartLiveResize()`](nsview/viewwillstartliveresize().md) and should clean up these data structures in [`viewDidEndLiveResize()`](nsview/viewdidendliveresize().md). In addition, a view that does optimized drawing during live resize might need to do full drawing after [`viewDidEndLiveResize()`](nsview/viewdidendliveresize().md). However, you should not assume that a view has a drawing context in [`viewDidEndLiveResize()`](nsview/viewdidendliveresize().md) (since it may have been removed from the window during live resize). A view that needs to redraw itself after live resize should set its [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/swift/true) in [`viewDidEndLiveResize()`](nsview/viewdidendliveresize().md).

A view subclass should call `super` from these methods.

## See Also

- [var inLiveResize: Bool](nsview/inliveresize.md)
  A Boolean value indicating whether the view is being rendered as part of a live resizing operation.
- [var preservesContentDuringLiveResize: Bool](nsview/preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](nsview/getrectsexposedduringliveresize(_:count:).md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [var rectPreservedDuringLiveResize: NSRect](nsview/rectpreservedduringliveresize.md)
  The rectangle identifying the portion of your view that did not change during a live resize operation.
- [func viewDidEndLiveResize()](nsview/viewdidendliveresize.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewwillstartliveresize())*