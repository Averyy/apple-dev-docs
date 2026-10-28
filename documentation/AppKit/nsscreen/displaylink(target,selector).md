# displayLink(target:selector:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new display link whose callback will be invoked in-sync with the display the screen is on.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func displayLink(target: Any, selector: Selector) -> CADisplayLink
```

```objc
- (CADisplayLink *) displayLinkWithTarget:(id) target selector:(SEL) selector;
```

## Discussion

Note that views and windows can move between screens and you may want to get a display link directly from `NSView` or `NSWindow` which will track those changes automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/displaylink(target:selector:))*