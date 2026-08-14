# SFSafariPage

**Framework**: Safari Services  
**Kind**: class

A proxy for a Safari webpage.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariPage
```

#### Overview

Use an `SFSafariPage` object in your Safari app extension to send messages to injected content scripts, access page properties, and reload the page.

## Topics

### Messaging Injected Scripts
- [func dispatchMessageToScript(withName: String, userInfo: [String : Any]?)](sfsafaripage/dispatchmessagetoscript(withname:userinfo:).md)
  Dispatches a message from the app extension to the content script injected in this page.
### Getting Page Information
- [func getPropertiesWithCompletionHandler((SFSafariPageProperties?) -> Void)](sfsafaripage/getpropertieswithcompletionhandler(_:).md)
  Retrieves the properties of the webpage.
### Reloading the Page
- [func reload()](sfsafaripage/reload.md)
  Tells Safari to reload the webpage.
### Instance Methods
- [func getContainingTab(completionHandler: (SFSafariTab) -> Void)](sfsafaripage/getcontainingtab(completionhandler:).md)
- [func getScreenshotOfVisibleArea(completionHandler: (NSImage?) -> Void)](sfsafaripage/getscreenshotofvisiblearea(completionhandler:).md)
### Initializers
- [init?(coder: NSCoder)](sfsafaripage/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Safari app extensions](safari-app-extensions.md)
  Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- [class SFSafariExtension](sfsafariextension.md)
  A proxy for the Safari extension.
- [class SFSafariApplication](sfsafariapplication.md)
  A proxy for the Safari app.
- [class SFSafariWindow](sfsafariwindow.md)
  A proxy for a Safari window.
- [class SFSafariTab](sfsafaritab.md)
  A proxy for a tab in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage)*