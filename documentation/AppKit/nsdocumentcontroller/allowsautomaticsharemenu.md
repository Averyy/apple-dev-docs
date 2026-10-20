# allowsAutomaticShareMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that the system uses to insert a Share menu in the File menu.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var allowsAutomaticShareMenu: Bool { get }
```

```objc
@property (readonly) BOOL allowsAutomaticShareMenu;
```

#### Discussion

If your application has any [`NSDocument`](../nsdocument.md) subclasses with [`autosavesInPlace`](../nsdocument/autosavesinplace.md) set to `true`, the system defaults `allowsAutomaticShareMenu` to `true`. To disable the Share menu entirely, or to enable custom placement or construction of the share menu, override this property to return `false` in your app.

The system may not insert a Share menu if `allowsAutomaticShareMenu` is `true` and [`NSDocumentController`](../nsdocumentcontroller.md) detects that the app has a Share menu.

## See Also

### Sharing
- [func standardShareMenuItem() -> NSMenuItem](./standardsharemenuitem%28%29.md)
  Returns a menu item that your app uses for sharing the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/allowsautomaticsharemenu)*