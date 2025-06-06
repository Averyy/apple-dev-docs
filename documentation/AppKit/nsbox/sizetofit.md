# sizeToFit()

**Framework**: AppKit  
**Kind**: method

Resizes and moves the receiver’s content view so it just encloses its subviews.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sizeToFit()
```

#### Discussion

The receiver is then moved and resized to wrap around the content view. The receiver’s width is constrained so its title will be fully displayed.

You should invoke this method after:

- Adding a subview (to the content view)
- Altering the size or location of such a subview
- Setting the margins around the content view

The mechanism by which the content view is moved and resized depends on whether the object responds to its own `sizeToFit` message: If it does respond, then that message is sent, and the content view is expected to be so modified. If the content view doesn’t respond, the box moves and resizes the content view itself.

## See Also

- [func setFrameFromContentFrame(NSRect)](nsbox/setframefromcontentframe(_:).md)
  Places the receiver so its content view lies on the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/sizetofit())*