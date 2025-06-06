# Documents, data, and pasteboard

**Framework**: UIKit

Organize your app’s data and share that data on the pasteboard.

## Topics

### Documents
- [class UIDocument](uidocument.md)
  An abstract base class for managing discrete portions of your app’s data.
- [class UIManagedDocument](uimanageddocument.md)
  A managed document object that integrates with Core Data.
- [Synchronizing documents in the iCloud environment](synchronizing-documents-in-the-icloud-environment.md)
  Manage documents across multiple devices to create a seamless editing and collaboration experience.
### Document presentation
- [class UIDocumentViewController](uidocumentviewcontroller.md)
  A view controller that manages and presents a document stored locally or in the cloud.
### Data management
- [protocol UIDataSourceModelAssociation](uidatasourcemodelassociation.md)
  A set of methods that defines an interface for providing persistent references to data objects in your app.
### Pasteboard
- [class UIPasteControl](uipastecontrol.md)
  A button that a person taps to place pasteboard contents in your app.
- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
- [class UIPasteboard](uipasteboard.md)
  An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.

## See Also

- [App and environment](app-and-environment.md)
  Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.
- [Resource management](resource-management.md)
  Manage the images, strings, storyboards, and nib files that you use to implement your app’s interface.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.
- [Interprocess communication](interprocess-communication.md)
  Display activity-based services to people.
- [Mac Catalyst](mac-catalyst.md)
  Create a version of your iPad app that users can run on a Mac device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/documents-data-and-pasteboard)*