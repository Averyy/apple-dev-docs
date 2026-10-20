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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/globalframedidchangenotification)*