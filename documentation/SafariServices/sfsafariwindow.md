# SFSafariWindow

**Framework**: Safari Services  
**Kind**: class

A proxy for a Safari window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariWindow
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

## Topics

### Working with Tabs
- [func getActiveTab(completionHandler: (SFSafariTab?) -> Void)](sfsafariwindow/getactivetab(completionhandler:).md)
  Calls the completion handler with the active tab in the target window.
- [func openTab(with: URL, makeActiveIfPossible: Bool, completionHandler: ((SFSafariTab?) -> Void)?)](sfsafariwindow/opentab(with:makeactiveifpossible:completionhandler:).md)
  Opens a tab at the end of the tab bar.
### Getting the Toolbar Item
- [func getToolbarItem(completionHandler: (SFSafariToolbarItem?) -> Void)](sfsafariwindow/gettoolbaritem(completionhandler:).md)
  Gets the extension’s toolbar item from the target window.
### Instance Methods
- [func close()](sfsafariwindow/close.md)
- [func getAllTabs(completionHandler: ([SFSafariTab]) -> Void)](sfsafariwindow/getalltabs(completionhandler:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Safari app extensions](safari-app-extensions.md)
  Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- [class SFSafariExtension](sfsafariextension.md)
  A proxy for the Safari extension.
- [class SFSafariApplication](sfsafariapplication.md)
  A proxy for the Safari app.
- [class SFSafariPage](sfsafaripage.md)
  A proxy for a Safari webpage.
- [class SFSafariTab](sfsafaritab.md)
  A proxy for a tab in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow)*