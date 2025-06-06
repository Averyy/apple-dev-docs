# viewWillTransition(to:)

**Framework**: AppKit  
**Kind**: method

For a view controller that is part of an app extension, called when its view is about to be resized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewWillTransition(to newSize: NSSize)
```

#### Discussion

Override this method if you want to change layout in response to the change in size, potentially in an animated way.

## Parameters

- `newSize`: The new size for the view controller’s view.

## See Also

- [var extensionContext: NSExtensionContext?](nsviewcontroller/extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredScreenOrigin: NSPoint](nsviewcontroller/preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](nsviewcontroller/preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](nsviewcontroller/preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [var sourceItemView: NSView?](nsviewcontroller/sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewwilltransition(to:))*