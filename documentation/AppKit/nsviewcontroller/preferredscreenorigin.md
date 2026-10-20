# preferredScreenOrigin

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

For a view controller that is part of an app extension, the preferred screen origin.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var preferredScreenOrigin: NSPoint { get set }
```

```objc
@property NSPoint preferredScreenOrigin;
```

#### Discussion

Set this property to position the lower-left corner of the app extension’s  primary view in screen space. To specify the desired primary view size for an app extension’s view controller, use the [`preferredContentSize`](./preferredcontentsize.md) property.

## See Also

### Related Documentation
- [var preferredContentSize: NSSize](./preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
### Configuring an App Extension View Controller
- [var extensionContext: NSExtensionContext?](./extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredMaximumSize: NSSize](./preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](./preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](./viewwilltransition%28to%29.md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](./sourceitemview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/preferredscreenorigin)*