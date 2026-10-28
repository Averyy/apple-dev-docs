# extensionContext

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

For a view controller that is part of an app extension, the app extension context.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var extensionContext: NSExtensionContext? { get }
```

```objc
@property (retain, readonly, nullable) NSExtensionContext * extensionContext;
```

## Discussion

If the view controller is *not* part of an app extension, the value of this property is `nil`.

By checking for `nil` you can employ this method to determine whether the view controller is part of an app or an app extension, for the purpose of conditionalizing your view controller implementation. Refer to [`NSExtensionContext`](../../Foundation/nsextensioncontext.md) for information about the extension context.

## See Also

### Configuring an App Extension View Controller
- [var preferredScreenOrigin: NSPoint](./preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](./preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](./preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](./viewwilltransition%28to%29.md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](./sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/extensioncontext)*