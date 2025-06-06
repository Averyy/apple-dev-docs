# viewBoundsChanged(_:)

**Framework**: AppKit  
**Kind**: method

Handles an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](nsscrollview.md) based on the new bounds.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func viewBoundsChanged(_ notification: Notification)
```

## See Also

- [func viewFrameChanged(Notification)](nsclipview/viewframechanged(_:).md)
  Handles an [`frameDidChangeNotification`](nsview/framedidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](nsscrollview.md) based on the new frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/viewboundschanged(_:))*