# SFSafariApplication

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A proxy for the Safari app.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariApplication
```

```objc
@interface SFSafariApplication : NSObject
```

## Overview

The `SFSafariApplication` class is used by a Safari app extension to access the active Safari window, open a new window, and update the toolbar items on a window. An application that acts as a host container for a Safari app extension can use this class to send messages to the app extension. There is no object instance for this class.

## Topics

### Communicating With the App Extension
- [class func dispatchMessage(withName: String, toExtensionWithIdentifier: String, userInfo: [String : Any]?, completionHandler: (((any Error)?) -> Void)?)](./sfsafariapplication/dispatchmessage%28withname,toextensionwithidentifier,userinfo,completionhandler%29.md)
  Sends a message to a Safari app extension, launching Safari if necessary.
### Working with Windows
- [class func getActiveWindow(completionHandler: (SFSafariWindow?) -> Void)](./sfsafariapplication/getactivewindow%28completionhandler%29.md)
  Calls the completion handler with the active browser window.
- [class func openWindow(with: URL, completionHandler: ((SFSafariWindow?) -> Void)?)](./sfsafariapplication/openwindow%28with,completionhandler%29.md)
  Opens a new window with the desired webpage.
- [class func showPreferencesForExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](./sfsafariapplication/showpreferencesforextension%28withidentifier,completionhandler%29.md)
  Launches Safari and opens the preferences panel for a Safari app extension.
### Updating Toolbar Items
- [class func setToolbarItemsNeedUpdate()](./sfsafariapplication/settoolbaritemsneedupdate%28%29.md)
  Updates the enabled states and badges of toolbar items.
### Type Methods
- [class func getAllWindows(completionHandler: ([SFSafariWindow]) -> Void)](./sfsafariapplication/getallwindows%28completionhandler%29.md)
- [class func getHostApplication(completionHandler: (NSRunningApplication) -> Void)](./sfsafariapplication/gethostapplication%28completionhandler%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Safari app extensions
- [Safari app extensions](./safari-app-extensions.md)
  Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- [class SFSafariExtension](./sfsafariextension.md)
  A proxy for the Safari extension.
- [class SFSafariWindow](./sfsafariwindow.md)
  A proxy for a Safari window.
- [class SFSafariPage](./sfsafaripage.md)
  A proxy for a Safari webpage.
- [class SFSafariTab](./sfsafaritab.md)
  A proxy for a tab in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication)*