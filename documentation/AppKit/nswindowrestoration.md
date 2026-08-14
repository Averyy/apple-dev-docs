# NSWindowRestoration

**Framework**: AppKit  
**Kind**: protocol

A set of methods that restoration classes must implement to handle the recreation of windows.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSWindowRestoration : NSObjectProtocol
```

#### Overview

At launch time, the application object retrieves the restoration class and uses its [`restoreWindow(withIdentifier:state:completionHandler:)`](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md) method to obtain a new window whose type matches the type that was preserved previously. Classes that adopt this protocol can use the provided information to create (or obtain a reference to) the window in the new application. As part of creating the window, the class should also create any related objects, such as window controllers, normally used to manage the window.

## Topics

### Handling Window Restoration
- [static func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md)
  Asks the class to provide a new window for the specified identifier.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
### Conforming Types
- [NSDocumentController](nsdocumentcontroller.md)

## See Also

- [Restoring your app’s state with AppKit](restoring-your-app-s-state-with-appkit.md)
  Provide continuity for people using your app by preserving current activities on macOS.
- [protocol NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
  A set of methods used to associate a unique identifier with objects in your user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowrestoration)*