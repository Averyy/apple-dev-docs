# preferredMaximumSize

**Framework**: AppKit  
**Kind**: property

For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var preferredMaximumSize: NSSize { get }
```

#### Discussion

An app extension should return the maximum dimensions that are potentially useful for its root view, based on the items the service has been sent.  By default, the value of this property is a large or infinite size.

## See Also

- [var preferredContentSize: NSSize](nsviewcontroller/preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
- [var extensionContext: NSExtensionContext?](nsviewcontroller/extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredScreenOrigin: NSPoint](nsviewcontroller/preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMinimumSize: NSSize](nsviewcontroller/preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](nsviewcontroller/viewwilltransition(to:).md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](nsviewcontroller/sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredmaximumsize)*