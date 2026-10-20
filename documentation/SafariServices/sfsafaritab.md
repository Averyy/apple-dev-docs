# SFSafariTab

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A proxy for a tab in a Safari window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariTab
```

```objc
@interface SFSafariTab : NSObject
```

## Topics

### Accessing Pages
- [func getActivePage(completionHandler: (SFSafariPage?) -> Void)](./sfsafaritab/getactivepage%28completionhandler%29.md)
  Calls the completion handler passing the active page in the tab.
- [func getPagesWithCompletionHandler(([SFSafariPage]?) -> Void)](./sfsafaritab/getpageswithcompletionhandler%28_%29.md)
  Calls the completion handler with all of the tab’s active and preloading pages.
### Activating Tabs
- [func activate(completionHandler: (() -> Void)?)](./sfsafaritab/activate%28completionhandler%29.md)
  Activates the tab.
### Instance Methods
- [func close()](./sfsafaritab/close%28%29.md)
- [func getContainingWindow(completionHandler: (SFSafariWindow?) -> Void)](./sfsafaritab/getcontainingwindow%28completionhandler%29.md)
- [func navigate(to: URL)](./sfsafaritab/navigate%28to%29.md)
### Initializers
- [init?(coder: NSCoder)](./sfsafaritab/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Safari app extensions
- [Safari app extensions](./safari-app-extensions.md)
  Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- [class SFSafariExtension](./sfsafariextension.md)
  A proxy for the Safari extension.
- [class SFSafariApplication](./sfsafariapplication.md)
  A proxy for the Safari app.
- [class SFSafariWindow](./sfsafariwindow.md)
  A proxy for a Safari window.
- [class SFSafariPage](./sfsafaripage.md)
  A proxy for a Safari webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab)*