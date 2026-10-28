# rectPreservedDuringLiveResize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle identifying the portion of your view that did not change during a live resize operation.

**Availability**:
- macOS

## Declaration

```swift
var rectPreservedDuringLiveResize: NSRect { get }
```

```objc
@property (readonly) NSRect rectPreservedDuringLiveResize;
```

## Discussion

The rectangle in this property is in the coordinate system of your view and reflects the space your view previously occupied. This rectangle may be smaller or the same size as your view’s current bounds, depending on whether the view grew or shrunk.

If your view does not support content preservation during live resizing, the rectangle will be empty. To support content preservation, override the [`preservesContentDuringLiveResize`](./preservescontentduringliveresize.md) property in your view and have your implementation return [`true`](../../Swift/true.md).

> **Note**:  The window containing your view must also support content preservation. To enable support for this feature in your window, use the [`preservesContentDuringLiveResize`](../nswindow/preservescontentduringliveresize.md) method of `NSWindow`.

## See Also

### Managing Live Resize
- [var inLiveResize: Bool](./inliveresize.md)
  A Boolean value indicating whether the view is being rendered as part of a live resizing operation.
- [var preservesContentDuringLiveResize: Bool](./preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](./getrectsexposedduringliveresize%28_,count%29.md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [func viewWillStartLiveResize()](./viewwillstartliveresize%28%29.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](./viewdidendliveresize%28%29.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rectpreservedduringliveresize)*