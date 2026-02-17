# displayLink(target:selector:)

**Framework**: AppKit  
**Kind**: method

Returns a new display link whose callback will be invoked in-sync with the display the view is on.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func displayLink(target: Any, selector: Selector) -> CADisplayLink
```

#### Discussion

If the view is hidden, or not on any display, the callback will not be invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/displaylink(target:selector:))*