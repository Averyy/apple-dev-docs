# flashScrollers()

**Framework**: AppKit  
**Kind**: method

Flash the overlay scroll bars.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func flashScrollers()
```

#### Discussion

This method only applies to scroll views that use overlay scrollers.

This method can be invoked to cause the overlay scroller knobs to be momentarily shown. This may be desirable when changing a document view’s size or swapping new content into the view, or to give the user a sense of the current position within the scrollable range at each step of an incremental search or similar operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/flashscrollers())*