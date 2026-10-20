# trackKnob(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tracks the knob and sends action messages to the receiver’s target.

**Availability**:
- macOS

## Declaration

```swift
func trackKnob(with event: NSEvent)
```

```objc
- (void) trackKnob:(NSEvent *) event;
```

#### Discussion

This method is invoked automatically when the receiver receives `theEvent` mouse-down event in the knob; you should not invoke it directly.

## See Also

### Event Handling
- [var hitPart: NSScroller.Part](./hitpart.md)
  A part code indicating the manner in which the scrolling should be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/trackknob(with:))*