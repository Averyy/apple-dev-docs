# restorationClass

**Framework**: AppKit  
**Kind**: property

The restoration class associated with the window.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var restorationClass: (any NSWindowRestoration.Type)? { get set }
```

#### Discussion

The value of this property is a class object that conforms to the [`NSWindowRestoration`](nswindowrestoration.md) protocol corresponding to the class to use to restore the window or `nil` if none is set.

The restoration class of a window is responsible for recreating not just the window but any other objects needed to manage the window. This almost always involves creating a window controller and for multi-window document applications also involves creating a document object. Therefore, the restoration class must be able to create (or find existing instances of) all of these objects at launch time in your application. When prompted by AppKit, the restoration class creates or acquires a window that matches the same type that was preserved. It then passes that window back to AppKit, which proceeds to reconfigure the window with the preserved state information.

If you mark your windows as restorable, you must associate a restoration class with them. For multi-window document applications, AppKit associates the [`NSDocumentController`](nsdocumentcontroller.md) class with any document windows by default. That class recreates the preserved document objects, which in turn recreate the corresponding window controller and window objects. For other types of windows, you must set the restoration class explicitly.

## See Also

- [var isRestorable: Bool](nswindow/isrestorable.md)
  A Boolean value indicating whether the window configuration is preserved between application launches.
- [func disableSnapshotRestoration()](nswindow/disablesnapshotrestoration.md)
  Disables snapshot restoration.
- [func enableSnapshotRestoration()](nswindow/enablesnapshotrestoration.md)
  Enables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/restorationclass)*