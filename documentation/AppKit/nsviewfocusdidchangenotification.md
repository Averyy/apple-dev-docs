# NSViewFocusDidChangeNotification

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Deprecated in macOS 10.4 and later. Posted for an `NSView` object and each of its descendants (recursively) whenever the frame or bounds geometry of the view changed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```c
extern NSNotificationName NSViewFocusDidChangeNotification;
```

## Discussion

Instead use `NSViewBoundsDidChangeNotification` and `NSViewFrameDidChangeNotification` to get the same information provided by this notification.

The notification object is the view whose geometry changed. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation
- [class let frameDidChangeNotification: NSNotification.Name](./nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [class let boundsDidChangeNotification: NSNotification.Name](./nsview/boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
### Deprecated notifications
- [NSViewNoInstrinsicMetric](./nsviewnoinstrinsicmetric.md)
  Used to indicate that a view has no intrinsic metric for a given numeric property.
- [class let globalFrameDidChangeNotification: NSNotification.Name](./nsview/globalframedidchangenotification.md)
  Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewfocusdidchangenotification)*