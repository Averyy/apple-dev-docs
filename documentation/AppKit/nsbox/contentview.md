# contentView

**Framework**: AppKit  
**Kind**: property

The receiver’s content view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```

#### Discussion

The content view of the `NSBox` object. The content view is created automatically when the box is created and resized as the box is resized (you should never send frame-altering messages directly to a box’s content view). You can replace it with an `NSView` of your own.

## See Also

- [var contentViewMargins: NSSize](nsbox/contentviewmargins.md)
  The distances between the border and the content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/contentview)*