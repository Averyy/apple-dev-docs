# viewBoundsChanged(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles an [`boundsDidChangeNotification`](../nsview/boundsdidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](../nsscrollview.md) based on the new bounds.

**Availability**:
- macOS

## Declaration

```swift
func viewBoundsChanged(_ notification: Notification)
```

```objc
- (void) viewBoundsChanged:(NSNotification *) notification;
```

## See Also

### Overriding NSView Methods
- [func viewFrameChanged(Notification)](./viewframechanged%28_%29.md)
  Handles an [`frameDidChangeNotification`](../nsview/framedidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](../nsscrollview.md) based on the new frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/viewboundschanged(_:))*