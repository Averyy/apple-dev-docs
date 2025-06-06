# scrollerStyle

**Framework**: AppKit  
**Kind**: property

The scroller style for this scroller.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var scrollerStyle: NSScroller.Style { get set }
```

#### Discussion

For a scroller that’s managed by an [`NSScrollView`](nsscrollview.md) object, the setter is automatically invoked by the scroll view with the appropriate setting, according to the user’s Appearance preference settings and possibly what pointing device(s) are present (see [`preferredScrollerStyle`](nsscroller/preferredscrollerstyle.md)).

For a list of valid scroller styles, see [`NSScroller.Style`](nsscroller/style.md).

## See Also

- [class var preferredScrollerStyle: NSScroller.Style](nsscroller/preferredscrollerstyle.md)
  Returns the style of scrollers that applications should use wherever possible.
- [var knobStyle: NSScroller.KnobStyle](nsscroller/knobstyle-swift.property.md)
  The scroller’s knob style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/scrollerstyle)*