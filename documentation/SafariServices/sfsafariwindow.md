# SFSafariWindow

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A proxy for a Safari window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariWindow
```

```objc
@interface SFSafariWindow : NSObject
```

## Mentions

- [Adjusting settings for a toolbar item](./adjusting-settings-for-a-toolbar-item.md)

## Topics

### Working with Tabs
- [func getActiveTab(completionHandler: (SFSafariTab?) -> Void)](./sfsafariwindow/getactivetab%28completionhandler%29.md)
  Calls the completion handler with the active tab in the target window.
- [func openTab(with: URL, makeActiveIfPossible: Bool, completionHandler: ((SFSafariTab?) -> Void)?)](./sfsafariwindow/opentab%28with,makeactiveifpossible,completionhandler%29.md)
  Opens a tab at the end of the tab bar.
### Getting the Toolbar Item
- [func getToolbarItem(completionHandler: (SFSafariToolbarItem?) -> Void)](./sfsafariwindow/gettoolbaritem%28completionhandler%29.md)
  Gets the extension’s toolbar item from the target window.
### Instance Methods
- [func close()](./sfsafariwindow/close%28%29.md)
- [func getAllTabs(completionHandler: ([SFSafariTab]) -> Void)](./sfsafariwindow/getalltabs%28completionhandler%29.md)
### Initializers
- [init?(coder: NSCoder)](./sfsafariwindow/init%28coder%29.md)

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
- [class SFSafariPage](./sfsafaripage.md)
  A proxy for a Safari webpage.
- [class SFSafariTab](./sfsafaritab.md)
  A proxy for a tab in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow)*