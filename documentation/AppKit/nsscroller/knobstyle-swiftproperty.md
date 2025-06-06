# knobStyle

**Framework**: AppKit  
**Kind**: property

The scroller’s knob style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var knobStyle: NSScroller.KnobStyle { get set }
```

#### Discussion

The value of this property does not affect legacy scrollers. [`NSScroller.KnobStyle.default`](nsscroller/knobstyle-swift.enum/default.md) is appropriate for a wide range of content, but in some cases choosing an alternative knob style may enhance visibility of the scroller knob atop some kinds of content.

For a list of possible values, see [`NSScroller.KnobStyle`](nsscroller/knobstyle-swift.enum.md).

## See Also

- [class var preferredScrollerStyle: NSScroller.Style](nsscroller/preferredscrollerstyle.md)
  Returns the style of scrollers that applications should use wherever possible.
- [var scrollerStyle: NSScroller.Style](nsscroller/scrollerstyle.md)
  The scroller style for this scroller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/knobstyle-swift.property)*