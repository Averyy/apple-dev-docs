# documentVisibleRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The exposed rectangle of the clip view’s document view, in the document view’s own coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var documentVisibleRect: NSRect { get }
```

```objc
@property (readonly) NSRect documentVisibleRect;
```

## Discussion

Note that this rectangle doesn’t reflect the effects of any clipping that may occur above the [`NSClipView`](../nsclipview.md) itself. To get the portion of the document view that’s guaranteed to be visible, send it a `visibleRect` message.

## See Also

### Accessing the Visible Portion
- [var documentRect: NSRect](./documentrect.md)
  The rectangle defining the document view’s frame, adjusted to the size of the clip view if the document view is smaller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/documentvisiblerect)*