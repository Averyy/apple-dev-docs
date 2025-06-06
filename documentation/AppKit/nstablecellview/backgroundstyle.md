# backgroundStyle

**Framework**: AppKit  
**Kind**: property

This property is automatically set by the enclosing row view to let this view know what its background looks like.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var backgroundStyle: NSView.BackgroundStyle { get set }
```

#### Discussion

The property is automatically set by the enclosing [`NSTableRowView`](nstablerowview.md) to let this view know what its background looks like. For instance, when the `backgroundStyle` is NSBackgroundStyleDark, the view should use a light text color.

The default implementation automatically forwards calls to all subviews that implement `setBackgroundStyle:` or are an NSControl, which have `NSCell` classes that respond to [`backgroundStyle`](nscell/backgroundstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/backgroundstyle)*