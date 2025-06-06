# NSHelpManager

**Framework**: AppKit  
**Kind**: class

An object for displaying online help for an app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSHelpManager
```

#### Overview

The [`NSHelpManager`](nshelpmanager.md) class provides an approach to displaying online help. An app contains one [`NSHelpManager`](nshelpmanager.md) object.

## Topics

### Getting the Help Manager
- [class var shared: NSHelpManager](nshelpmanager/shared.md)
  Returns the shared [`NSHelpManager`](nshelpmanager.md) instance, creating it if it does not already exist.
### Displaying Help
- [func find(String, inBook: NSHelpManager.BookName?)](nshelpmanager/find(_:inbook:).md)
  Performs a search for the specified string in the specified book.
- [func openHelpAnchor(NSHelpManager.AnchorName, inBook: NSHelpManager.BookName?)](nshelpmanager/openhelpanchor(_:inbook:).md)
  Finds and displays the text at the given anchor location in the given book.
- [NSHelpManager.AnchorName](nshelpmanager/anchorname.md)
- [NSHelpManager.BookName](nshelpmanager/bookname.md)
### Dynamically Adding Help Books
- [func registerBooks(in: Bundle) -> Bool](nshelpmanager/registerbooks(in:).md)
  Registers one or more help books in the given bundle.
### Configuring Context-Sensitive Help
- [func setContextHelp(NSAttributedString, for: Any)](nshelpmanager/setcontexthelp(_:for:).md)
  Associates help content with an object.
- [func removeContextHelp(for: Any)](nshelpmanager/removecontexthelp(for:).md)
  Removes the association between an object and its context-sensitive help.
### Displaying Context-Sensitive Help
- [func contextHelp(for: Any) -> NSAttributedString?](nshelpmanager/contexthelp(for:).md)
  Returns context-sensitive help for an object.
- [func showContextHelp(for: Any, locationHint: NSPoint) -> Bool](nshelpmanager/showcontexthelp(for:locationhint:).md)
  Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.
- [NSHelpManager.ContextHelpKey](nshelpmanager/contexthelpkey.md)
- [class var isContextHelpModeActive: Bool](nshelpmanager/iscontexthelpmodeactive.md)
### Notifications
- [class let contextHelpModeDidActivateNotification: NSNotification.Name](nshelpmanager/contexthelpmodedidactivatenotification.md)
  Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.
- [class let contextHelpModeDidDeactivateNotification: NSNotification.Name](nshelpmanager/contexthelpmodediddeactivatenotification.md)
  Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSUserInterfaceItemSearching](nsuserinterfaceitemsearching.md)
  A set of methods an app can implement to provide Spotlight for Help for its own custom help data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager)*