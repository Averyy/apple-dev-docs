# SFSafariExtensionHandling

**Framework**: Safari Services  
**Kind**: protocol

A protocol for implementing event handling in a Safari app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
protocol SFSafariExtensionHandling : NSObjectProtocol
```

## Topics

### Receiving Messages in Your App Extension
- [func messageReceived(withName: String, from: SFSafariPage, userInfo: [String : Any]?)](sfsafariextensionhandling/messagereceived(withname:from:userinfo:).md)
  A method the system calls when the extension receives a message from an injected script.
- [func messageReceivedFromContainingApp(withName: String, userInfo: [String : Any]?)](sfsafariextensionhandling/messagereceivedfromcontainingapp(withname:userinfo:).md)
  A method the system calls when the extension receives a message from the extension’s containing app.
### Responding to Context Menu Selections
- [func contextMenuItemSelected(withCommand: String, in: SFSafariPage, userInfo: [String : Any]?)](sfsafariextensionhandling/contextmenuitemselected(withcommand:in:userinfo:).md)
  A method the system calls when a user selects one of the app extension’s context menu items.
- [func validateContextMenuItem(withCommand: String, in: SFSafariPage, userInfo: [String : Any]?, validationHandler: (Bool, String?) -> Void)](sfsafariextensionhandling/validatecontextmenuitem(withcommand:in:userinfo:validationhandler:).md)
  Validates whether a particular contextual menu item should be displayed.
### Working with Toolbar Items
- [func toolbarItemClicked(in: SFSafariWindow)](sfsafariextensionhandling/toolbaritemclicked(in:).md)
  A method the system calls when a user clicks a toolbar item associated with the app extension.
- [func validateToolbarItem(in: SFSafariWindow, validationHandler: (Bool, String) -> Void)](sfsafariextensionhandling/validatetoolbaritem(in:validationhandler:).md)
  Determines if a toolbar menu item should be enabled or have badge text when browser state changes.
### Working with Popovers
- [func popoverViewController() -> SFSafariExtensionViewController](sfsafariextensionhandling/popoverviewcontroller.md)
  Asks the handler to provide a popover view controller for display.
- [func popoverWillShow(in: SFSafariWindow)](sfsafariextensionhandling/popoverwillshow(in:).md)
  Tells the handler that the app extension’s popover is about to be opened.
- [func popoverDidClose(in: SFSafariWindow)](sfsafariextensionhandling/popoverdidclose(in:).md)
  Tells the handler that the app extension’s popover was closed.
### Working with Content Blockers
- [func contentBlocker(withIdentifier: String, blockedResourcesWith: [URL], on: SFSafariPage)](sfsafariextensionhandling/contentblocker(withidentifier:blockedresourceswith:on:).md)
  Tells the handler which resources a content blocker blocked on a webpage.
### Responding to Page Navigation
- [func page(SFSafariPage, willNavigateTo: URL?)](sfsafariextensionhandling/page(_:willnavigateto:).md)
  A method the system calls when a webpage is about to navigate to a new URL.
### Instance Methods
- [func additionalRequestHeaders(for: URL, completionHandler: ([String : String]?) -> Void)](sfsafariextensionhandling/additionalrequestheaders(for:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SFSafariExtensionHandler](sfsafariextensionhandler.md)

## See Also

- [class func dispatchMessage(withName: String, toExtensionWithIdentifier: String, userInfo: [String : Any]?, completionHandler: (((any Error)?) -> Void)?)](sfsafariapplication/dispatchmessage(withname:toextensionwithidentifier:userinfo:completionhandler:).md)
  Sends a message to a Safari app extension, launching Safari if necessary.
- [Using injected style sheets and scripts](using-injected-style-sheets-and-scripts.md)
  Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.
- [Injecting a script into a webpage](injecting-a-script-into-a-webpage.md)
  Inject a script that you write for a Safari app extension into a webpage.
- [Injecting CSS style sheets into a webpage](injecting-css-style-sheets-into-a-webpage.md)
  Add to or override styles by injecting CSS style sheets into webpages.
- [Passing messages between Safari app extensions and injected scripts](passing-messages-between-safari-app-extensions-and-injected-scripts.md)
  Communicate between your Safari app extension and injected scripts.
- [class SFSafariExtensionHandler](sfsafariextensionhandler.md)
  A base class that you subclass to handle events in your Safari app extension.
- [class SFSafariExtensionManager](sfsafariextensionmanager.md)
  A class that your app uses to find out the current state of a Safari app extension.
- [class SFSafariExtensionState](sfsafariextensionstate.md)
  The state of a Safari app extension.
- [class SFSafariPageProperties](sfsafaripageproperties.md)
  An object that captures information about a webpage.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling)*