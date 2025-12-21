# rectPreservedDuringLiveResize

**Framework**: AppKit  
**Kind**: property

The rectangle identifying the portion of your view that did not change during a live resize operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rectPreservedDuringLiveResize: NSRect { get }
```

#### Discussion

The rectangle in this property is in the coordinate system of your view and reflects the space your view previously occupied. This rectangle may be smaller or the same size as your view’s current bounds, depending on whether the view grew or shrunk.

If your view does not support content preservation during live resizing, the rectangle will be empty. To support content preservation, override the [`preservesContentDuringLiveResize`](nsview/preservescontentduringliveresize.md) property in your view and have your implementation return [`true`](https://developer.apple.com/documentation/Swift/true).

> **Note**:  The window containing your view must also support content preservation. To enable support for this feature in your window, use the [`preservesContentDuringLiveResize`](nswindow/preservescontentduringliveresize.md) method of `NSWindow`.

## See Also

- [var inLiveResize: Bool](nsview/inliveresize.md)
  A Boolean value indicating whether the view is being rendered as part of a live resizing operation.
- [var preservesContentDuringLiveResize: Bool](nsview/preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](nsview/getrectsexposedduringliveresize(_:count:).md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [func viewWillStartLiveResize()](nsview/viewwillstartliveresize.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](nsview/viewdidendliveresize.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rectpreservedduringliveresize)*