# inLiveResize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view is being rendered as part of a live resizing operation.

**Availability**:
- macOS

## Declaration

```swift
var inLiveResize: Bool { get }
```

```objc
@property (readonly) BOOL inLiveResize;
```

#### Discussion

AppKit sets the value of this property to [`true`](../../Swift/true.md) when a live resizing operation involving the view is underway. Use this property to determine when to optimize your view’s drawing behavior. Typically, you access this property from your [`draw(_:)`](./draw%28_%29.md) method and use the value to change the fidelity of the content you draw, or to draw your content more efficiently.

## See Also

### Managing Live Resize
- [var preservesContentDuringLiveResize: Bool](./preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](./getrectsexposedduringliveresize%28_,count%29.md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [var rectPreservedDuringLiveResize: NSRect](./rectpreservedduringliveresize.md)
  The rectangle identifying the portion of your view that did not change during a live resize operation.
- [func viewWillStartLiveResize()](./viewwillstartliveresize%28%29.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](./viewdidendliveresize%28%29.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/inliveresize)*