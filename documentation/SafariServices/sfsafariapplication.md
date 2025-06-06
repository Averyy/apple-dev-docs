# SFSafariApplication

**Framework**: Safari Services  
**Kind**: class

A proxy for the Safari app.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariApplication
```

#### Overview

The `SFSafariApplication` class is used by a Safari app extension to access the active Safari window, open a new window, and update the toolbar items on a window. An application that acts as a host container for a Safari app extension can use this class to send messages to the app extension. There is no object instance for this class.

## Topics

### Communicating With the App Extension
- [class func dispatchMessage(withName: String, toExtensionWithIdentifier: String, userInfo: [String : Any]?, completionHandler: (((any Error)?) -> Void)?)](sfsafariapplication/dispatchmessage(withname:toextensionwithidentifier:userinfo:completionhandler:).md)
  Sends a message to a Safari app extension, launching Safari if necessary.
### Working with Windows
- [class func getActiveWindow(completionHandler: (SFSafariWindow?) -> Void)](sfsafariapplication/getactivewindow(completionhandler:).md)
  Calls the completion handler with the active browser window.
- [class func openWindow(with: URL, completionHandler: ((SFSafariWindow?) -> Void)?)](sfsafariapplication/openwindow(with:completionhandler:).md)
  Opens a new window with the desired webpage.
- [class func showPreferencesForExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](sfsafariapplication/showpreferencesforextension(withidentifier:completionhandler:).md)
  Launches Safari and opens the preferences panel for a Safari app extension.
### Updating Toolbar Items
- [class func setToolbarItemsNeedUpdate()](sfsafariapplication/settoolbaritemsneedupdate.md)
  Updates the enabled states and badges of toolbar items.
### Type Methods
- [class func getAllWindows(completionHandler: ([SFSafariWindow]) -> Void)](sfsafariapplication/getallwindows(completionhandler:).md)
- [class func getHostApplication(completionHandler: (NSRunningApplication) -> Void)](sfsafariapplication/gethostapplication(completionhandler:).md)

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

## See Also

- [Safari app extensions](safari-app-extensions.md)
  Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- [class SFSafariExtension](sfsafariextension.md)
  A proxy for the Safari extension.
- [class SFSafariWindow](sfsafariwindow.md)
  A proxy for a Safari window.
- [class SFSafariPage](sfsafaripage.md)
  A proxy for a Safari webpage.
- [class SFSafariTab](sfsafaritab.md)
  A proxy for a tab in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication)*