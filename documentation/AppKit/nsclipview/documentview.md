# documentView

**Framework**: AppKit  
**Kind**: property

The clip view’s document view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var documentView: NSView? { get set }
```

#### Discussion

If the clip view is contained in an [`NSScrollView`](nsscrollview.md), you should send the [`NSScrollView`](nsscrollview.md) a [`documentView`](nsscrollview/documentview.md) message instead, so it can perform whatever updating it needs. Setting this property to a view removes any previous document view, and sets the origin of the clip view’s bounds rectangle to the origin of the new view’s frame rectangle. Doing so also registers the clip view for the notifications [`frameDidChangeNotification`](nsview/framedidchangenotification.md) and [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md), adjusts the key view loop to include the new document view, and updates a parent [`NSScrollView`](nsscrollview.md) display if needed using [`reflectScrolledClipView(_:)`](nsscrollview/reflectscrolledclipview(_:).md).

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/documentview)*