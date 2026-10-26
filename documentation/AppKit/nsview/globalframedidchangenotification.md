# globalFrameDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use NSOpenGLView instead.

## Declaration

```swift
class let globalFrameDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSViewGlobalFrameDidChangeNotification;
```

#### Discussion

The notification object is the surface’s view. This notification does not contain a `userInfo` dictionary.

## See Also

### Deprecated notifications
- [NSViewNoInstrinsicMetric](../nsviewnoinstrinsicmetric.md)
  Used to indicate that a view has no intrinsic metric for a given numeric property.
- [NSViewFocusDidChangeNotification](../nsviewfocusdidchangenotification.md)
  Deprecated in macOS 10.4 and later. Posted for an `NSView` object and each of its descendants (recursively) whenever the frame or bounds geometry of the view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/globalframedidchangenotification)*