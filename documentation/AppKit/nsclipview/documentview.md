# documentView

**Framework**: AppKit  
**Kind**: property

The clip view’s document view.

**Availability**:
- macOS ?+

## Declaration

```swift
var documentView: NSView? { get set }
```

#### Discussion

If the clip view is contained in an [`NSScrollView`](nsscrollview.md), you should send the [`NSScrollView`](nsscrollview.md) a [`documentView`](nsscrollview/documentview.md) message instead, so it can perform whatever updating it needs. Setting this property to a view removes any previous document view, and sets the origin of the clip view’s bounds rectangle to the origin of the new view’s frame rectangle. Doing so also registers the clip view for the notifications [`frameDidChangeNotification`](nsview/framedidchangenotification.md) and [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md), adjusts the key view loop to include the new document view, and updates a parent [`NSScrollView`](nsscrollview.md) display if needed using [`reflectScrolledClipView(_:)`](nsscrollview/reflectscrolledclipview(_:).md).

## See Also

- [class NSClipView](nsclipview.md)
  An object that clips a document view to a scroll view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/documentview)*