# init(scrollView:orientation:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated NSRulerView to have `orientation` (`NSHorizontalRuler` or `NSVerticalRuler`) within `aScrollView`.

**Availability**:
- macOS

## Declaration

```swift
init(scrollView: NSScrollView?, orientation: NSRulerView.Orientation)
```

```objc
- (instancetype) initWithScrollView:(NSScrollView *) scrollView orientation:(NSRulerOrientation) orientation;
```

#### Discussion

The new ruler view displays the user’s preferred measurement units and has no client, markers, or accessory view. Unlike most subclasses of NSView, no initial frame rectangle is given for NSRulerView; its containing NSScrollView adjusts its frame rectangle as needed.

This method is the designated initializer for the NSRulerView class. Returns an initialized object.

## See Also

### Related Documentation
- [Ruler and Paragraph Style Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Rulers.html#//apple_ref/doc/uid/10000089i)
### Creating a Ruler View
- [init(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/init(scrollview:orientation:))*