# App extensions

**Framework**: UIKit

Extend your app’s basic functionality to other parts of the system.

## Topics

### Extension support
- [protocol NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
  The interface an app extension uses to respond to a request from a host app.
- [class NSExtensionContext](../Foundation/NSExtensionContext.md)
  The host app context from which an app extension is invoked.
### Document provider
- [class NSFileProviderExtension](../FileProvider/NSFileProviderExtension.md)
  The principal class for the nonreplicated File Provider extension.
- [class UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)
  The principal class for the Document Picker View Controller extension.
### Custom keyboard
- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.
- [protocol UIInputViewAudioFeedback](uiinputviewaudiofeedback.md)
  A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.

## See Also

- [App and environment](app-and-environment.md)
  Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.
- [Documents, data, and pasteboard](documents-data-and-pasteboard.md)
  Organize your app’s data and share that data on the pasteboard.
- [Resource management](resource-management.md)
  Manage the images, strings, storyboards, and nib files that you use to implement your app’s interface.
- [Interprocess communication](interprocess-communication.md)
  Display activity-based services to people.
- [Mac Catalyst](mac-catalyst.md)
  Create a version of your iPad app that users can run on a Mac device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/app-extensions)*