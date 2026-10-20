# viewFrameChanged(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles an [`frameDidChangeNotification`](../nsview/framedidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](../nsscrollview.md) based on the new frame.

**Availability**:
- macOS

## Declaration

```swift
func viewFrameChanged(_ notification: Notification)
```

```objc
- (void) viewFrameChanged:(NSNotification *) notification;
```

## See Also

### Overriding NSView Methods
- [func viewBoundsChanged(Notification)](./viewboundschanged%28_%29.md)
  Handles an [`boundsDidChangeNotification`](../nsview/boundsdidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](../nsscrollview.md) based on the new bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/viewframechanged(_:))*