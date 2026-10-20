# preferredMinimumSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var preferredMinimumSize: NSSize { get }
```

```objc
@property (readonly) NSSize preferredMinimumSize;
```

#### Discussion

An app extension should return the minimum dimensions its primary view can accommodate, based on the items the app extension has been sent. By default, the value of this property is a small but non-empty size.

## See Also

### Related Documentation
- [var preferredContentSize: NSSize](./preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
### Configuring an App Extension View Controller
- [var extensionContext: NSExtensionContext?](./extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredScreenOrigin: NSPoint](./preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](./preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](./viewwilltransition%28to%29.md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](./sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredminimumsize)*