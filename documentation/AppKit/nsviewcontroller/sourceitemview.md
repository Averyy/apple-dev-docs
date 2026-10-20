# sourceItemView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 10.10+

## Declaration

```swift
@IBOutlet
var sourceItemView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * sourceItemView;
```

## See Also

### Configuring an App Extension View Controller
- [var extensionContext: NSExtensionContext?](./extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredScreenOrigin: NSPoint](./preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](./preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](./preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](./viewwilltransition%28to%29.md)
  For a view controller that is part of an app extension, called when its view is about to be resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/sourceitemview)*