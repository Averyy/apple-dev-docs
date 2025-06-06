# preferredScreenOrigin

**Framework**: AppKit  
**Kind**: property

For a view controller that is part of an app extension, the preferred screen origin.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var preferredScreenOrigin: NSPoint { get set }
```

#### Discussion

Set this property to position the lower-left corner of the app extension’s  primary view in screen space. To specify the desired primary view size for an app extension’s view controller, use the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property.

## See Also

- [var preferredContentSize: NSSize](nsviewcontroller/preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
- [var extensionContext: NSExtensionContext?](nsviewcontroller/extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredMaximumSize: NSSize](nsviewcontroller/preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](nsviewcontroller/preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](nsviewcontroller/viewwilltransition(to:).md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](nsviewcontroller/sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredscreenorigin)*