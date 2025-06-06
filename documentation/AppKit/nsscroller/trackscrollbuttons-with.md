# trackScrollButtons(with:)

**Framework**: AppKit  
**Kind**: method

Tracks the scroll buttons and sends action messages to the receiver’s target.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func trackScrollButtons(with event: NSEvent)
```

#### Discussion

This method is invoked automatically when the receiver receives `theEvent` mouse-down event in a scroll button; you should not invoke this method directly.

##### Special Considerations

This method is not invoked in macOS 10.7 and later.

## See Also

- [var hitPart: NSScroller.Part](nsscroller/hitpart.md)
  A part code indicating the manner in which the scrolling should be performed.
- [func trackKnob(with: NSEvent)](nsscroller/trackknob(with:).md)
  Tracks the knob and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/trackscrollbuttons(with:))*