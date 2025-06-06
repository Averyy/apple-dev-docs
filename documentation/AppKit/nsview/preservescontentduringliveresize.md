# preservesContentDuringLiveResize

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var preservesContentDuringLiveResize: Bool { get }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). If your view supports content preservation, override this property and return [`true`](https://developer.apple.com/documentation/swift/true). Content preservation lets your view decide what to redraw during a live resize operation. If your view supports this feature, you should also provide a custom implementation of the [`setFrameSize(_:)`](nsview/setframesize(_:).md) method that invalidates the portions of your view that actually need to be redrawn.

For information on how to implement this feature in your views, see [`Cocoa Performance Guidelines`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/CocoaPerformance.html#//apple_ref/doc/uid/TP40001448).

## See Also

- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var inLiveResize: Bool](nsview/inliveresize.md)
  A Boolean value indicating whether the view is being rendered as part of a live resizing operation.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](nsview/getrectsexposedduringliveresize(_:count:).md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [var rectPreservedDuringLiveResize: NSRect](nsview/rectpreservedduringliveresize.md)
  The rectangle identifying the portion of your view that did not change during a live resize operation.
- [func viewWillStartLiveResize()](nsview/viewwillstartliveresize.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](nsview/viewdidendliveresize.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/preservescontentduringliveresize)*