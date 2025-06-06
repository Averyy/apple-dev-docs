# preferredMinimumSize

**Framework**: AppKit  
**Kind**: property

For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var preferredMinimumSize: NSSize { get }
```

#### Discussion

An app extension should return the minimum dimensions its primary view can accommodate, based on the items the app extension has been sent. By default, the value of this property is a small but non-empty size.

## See Also

- [var preferredContentSize: NSSize](nsviewcontroller/preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
- [var extensionContext: NSExtensionContext?](nsviewcontroller/extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredScreenOrigin: NSPoint](nsviewcontroller/preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](nsviewcontroller/preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](nsviewcontroller/viewwilltransition(to:).md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](nsviewcontroller/sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredminimumsize)*