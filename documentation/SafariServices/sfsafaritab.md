# SFSafariTab

**Framework**: Safari Services  
**Kind**: class

A proxy for a tab in a Safari window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariTab
```

## Topics

### Accessing Pages
- [func getActivePage(completionHandler: (SFSafariPage?) -> Void)](sfsafaritab/getactivepage(completionhandler:).md)
  Calls the completion handler passing the active page in the tab.
- [func getPagesWithCompletionHandler(([SFSafariPage]?) -> Void)](sfsafaritab/getpageswithcompletionhandler(_:).md)
  Calls the completion handler with all of the tab’s active and preloading pages.
### Activating Tabs
- [func activate(completionHandler: (() -> Void)?)](sfsafaritab/activate(completionhandler:).md)
  Activates the tab.
### Instance Methods
- [func close()](sfsafaritab/close.md)
- [func getContainingWindow(completionHandler: (SFSafariWindow?) -> Void)](sfsafaritab/getcontainingwindow(completionhandler:).md)
- [func navigate(to: URL)](sfsafaritab/navigate(to:).md)

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
- [class SFSafariWindow](sfsafariwindow.md)
  A proxy for a Safari window.
- [class SFSafariPage](sfsafaripage.md)
  A proxy for a Safari webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab)*