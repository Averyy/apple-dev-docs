# extensionContext

**Framework**: AppKit  
**Kind**: property

For a view controller that is part of an app extension, the app extension context.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var extensionContext: NSExtensionContext? { get }
```

#### Discussion

If the view controller is  part of an app extension, the value of this property is `nil`.

By checking for `nil` you can employ this method to determine whether the view controller is part of an app or an app extension, for the purpose of conditionalizing your view controller implementation. Refer to [`NSExtensionContext`](https://developer.apple.com/documentation/Foundation/NSExtensionContext) for information about the extension context.

## See Also

- [var preferredScreenOrigin: NSPoint](nsviewcontroller/preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](nsviewcontroller/preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](nsviewcontroller/preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](nsviewcontroller/viewwilltransition(to:).md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](nsviewcontroller/sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/extensioncontext)*