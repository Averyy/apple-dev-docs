# init(scrollView:orientation:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated NSRulerView to have `orientation` (`NSHorizontalRuler` or `NSVerticalRuler`) within `aScrollView`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(scrollView: NSScrollView?, orientation: NSRulerView.Orientation)
```

#### Discussion

The new ruler view displays the user’s preferred measurement units and has no client, markers, or accessory view. Unlike most subclasses of NSView, no initial frame rectangle is given for NSRulerView; its containing NSScrollView adjusts its frame rectangle as needed.

This method is the designated initializer for the NSRulerView class. Returns an initialized object.

## See Also

- [Ruler and Paragraph Style Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Rulers.html#//apple_ref/doc/uid/10000089i)
- [init(coder: NSCoder)](nsrulerview/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/init(scrollview:orientation:))*