# scrollerStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroller style for this scroller.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var scrollerStyle: NSScroller.Style { get set }
```

```objc
@property NSScrollerStyle scrollerStyle;
```

#### Discussion

For a scroller that’s managed by an [`NSScrollView`](../nsscrollview.md) object, the setter is automatically invoked by the scroll view with the appropriate setting, according to the user’s Appearance preference settings and possibly what pointing device(s) are present (see [`preferredScrollerStyle`](./preferredscrollerstyle.md)).

For a list of valid scroller styles, see [`NSScroller.Style`](./style.md).

## See Also

### Managing Presentation Style
- [class var preferredScrollerStyle: NSScroller.Style](./preferredscrollerstyle.md)
  Returns the style of scrollers that applications should use wherever possible.
- [var knobStyle: NSScroller.KnobStyle](./knobstyle-swift.property.md)
  The scroller’s knob style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/scrollerstyle)*