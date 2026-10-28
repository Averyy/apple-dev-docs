# SFSafariPage

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A proxy for a Safari webpage.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariPage
```

```objc
@interface SFSafariPage : NSObject
```

## Overview

Use an `SFSafariPage` object in your Safari app extension to send messages to injected content scripts, access page properties, and reload the page.

## Topics

### Messaging Injected Scripts
- [func dispatchMessageToScript(withName: String, userInfo: [String : Any]?)](./sfsafaripage/dispatchmessagetoscript%28withname,userinfo%29.md)
  Dispatches a message from the app extension to the content script injected in this page.
### Getting Page Information
- [func getPropertiesWithCompletionHandler((SFSafariPageProperties?) -> Void)](./sfsafaripage/getpropertieswithcompletionhandler%28_%29.md)
  Retrieves the properties of the webpage.
### Reloading the Page
- [func reload()](./sfsafaripage/reload%28%29.md)
  Tells Safari to reload the webpage.
### Instance Methods
- [func getContainingTab(completionHandler: (SFSafariTab) -> Void)](./sfsafaripage/getcontainingtab%28completionhandler%29.md)
- [func getScreenshotOfVisibleArea(completionHandler: (NSImage?) -> Void)](./sfsafaripage/getscreenshotofvisiblearea%28completionhandler%29.md)
### Initializers
- [init?(coder: NSCoder)](./sfsafaripage/init%28coder%29.md)

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
- [class SFSafariTab](./sfsafaritab.md)
  A proxy for a tab in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage)*