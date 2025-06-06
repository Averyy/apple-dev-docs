# inLiveResize

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view is being rendered as part of a live resizing operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var inLiveResize: Bool { get }
```

#### Discussion

AppKit sets the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) when a live resizing operation involving the view is underway. Use this property to determine when to optimize your view’s drawing behavior. Typically, you access this property from your [`draw(_:)`](nsview/draw(_:).md) method and use the value to change the fidelity of the content you draw, or to draw your content more efficiently.

## See Also

- [var preservesContentDuringLiveResize: Bool](nsview/preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](nsview/getrectsexposedduringliveresize(_:count:).md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [var rectPreservedDuringLiveResize: NSRect](nsview/rectpreservedduringliveresize.md)
  The rectangle identifying the portion of your view that did not change during a live resize operation.
- [func viewWillStartLiveResize()](nsview/viewwillstartliveresize.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](nsview/viewdidendliveresize.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/inliveresize)*