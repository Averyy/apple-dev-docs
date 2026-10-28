# getRectsExposedDuringLiveResize(_:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a list of rectangles indicating the newly exposed areas of the view.

**Availability**:
- macOS

## Declaration

```swift
func getRectsExposedDuringLiveResize(_ exposedRects: UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)
```

```objc
- (void) getRectsExposedDuringLiveResize:(NSRect[4]) exposedRects count:(NSInteger *) count;
```

## Discussion

If your view does not support content preservation during live resizing, the entire area of your view is returned in the `exposedRects` parameter. To support content preservation, override the [`preservesContentDuringLiveResize`](./preservescontentduringliveresize.md) property in your view and have your implementation return [`true`](../../Swift/true.md).

> **Note**:  The window containing your view must also support content preservation. To enable support for this feature in your window, use the [`preservesContentDuringLiveResize`](../nswindow/preservescontentduringliveresize.md) method of `NSWindow`.

If the view decreased in both height and width, the list of returned rectangles will be empty. If the view increased in both height and width and its upper-left corner stayed anchored in the same position, the list of returned rectangles will contain a vertical and horizontal component indicating the exposed area.

## Parameters

- `exposedRects`: On return, contains the list of rectangles. The returned rectangles are in the coordinate space of the view.
- `count`: Contains the number of rectangles in `exposedRects`; this value may be 0 and is guaranteed to be no more than 4.

## See Also

### Managing Live Resize
- [var inLiveResize: Bool](./inliveresize.md)
  A Boolean value indicating whether the view is being rendered as part of a live resizing operation.
- [var preservesContentDuringLiveResize: Bool](./preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [var rectPreservedDuringLiveResize: NSRect](./rectpreservedduringliveresize.md)
  The rectangle identifying the portion of your view that did not change during a live resize operation.
- [func viewWillStartLiveResize()](./viewwillstartliveresize%28%29.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](./viewdidendliveresize%28%29.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/getrectsexposedduringliveresize(_:count:))*