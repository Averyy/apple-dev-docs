# NSViewNoInstrinsicMetric

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Used to indicate that a view has no intrinsic metric for a given numeric property.

**Availability**:
- macOS 10.7+ - Deprecated in 10.14

## Declaration

```c
extern const CGFloat NSViewNoInstrinsicMetric;
```

## See Also

### Deprecated notifications
- [NSViewFocusDidChangeNotification](./nsviewfocusdidchangenotification.md)
  Deprecated in macOS 10.4 and later. Posted for an `NSView` object and each of its descendants (recursively) whenever the frame or bounds geometry of the view changed.
- [class let globalFrameDidChangeNotification: NSNotification.Name](./nsview/globalframedidchangenotification.md)
  Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewnoinstrinsicmetric)*