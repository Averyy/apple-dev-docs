# shared

**Framework**: AppKit  
**Kind**: property

Returns the shared instance of NSUserDefaultsController, creating it if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
class var shared: NSUserDefaultsController { get }
```

#### Discussion

This instance has no initial values, and uses `[NSUserDefaults standardUserDefaults]` to create the defaults. An application can get this object when an application launches and configure it as required.

## See Also

- [Cocoa Bindings Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller/shared)*