# trackKnob(with:)

**Framework**: AppKit  
**Kind**: method

Tracks the knob and sends action messages to the receiver’s target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func trackKnob(with event: NSEvent)
```

#### Discussion

This method is invoked automatically when the receiver receives `theEvent` mouse-down event in the knob; you should not invoke it directly.

## See Also

- [var hitPart: NSScroller.Part](nsscroller/hitpart.md)
  A part code indicating the manner in which the scrolling should be performed.
- [func trackScrollButtons(with: NSEvent)](nsscroller/trackscrollbuttons(with:).md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/trackknob(with:))*