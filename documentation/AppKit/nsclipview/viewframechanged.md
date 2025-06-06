# viewFrameChanged(_:)

**Framework**: AppKit  
**Kind**: method

Handles an [`frameDidChangeNotification`](nsview/framedidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](nsscrollview.md) based on the new frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func viewFrameChanged(_ notification: Notification)
```

## See Also

- [func viewBoundsChanged(Notification)](nsclipview/viewboundschanged(_:).md)
  Handles an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](nsscrollview.md) based on the new bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/viewframechanged(_:))*