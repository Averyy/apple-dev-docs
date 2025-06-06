# Cocoa Bindings

**Framework**: AppKit

Automatically synchronize your data model with your app’s interface using Cocoa Bindings.

## Topics

### Core Controllers
- [class NSObjectController](nsobjectcontroller.md)
  A controller that can manage an object’s properties referenced by key-value paths.
- [class NSController](nscontroller.md)
  An abstract class that implements the [`NSEditor`](nseditor.md) and [`NSEditorRegistration`](nseditorregistration.md) informal protocols required for controller classes.
### Tree-Based Data
- [Navigating Hierarchical Data Using Outline and Split Views](navigating-hierarchical-data-using-outline-and-split-views.md)
  Build a structured user interface that simplifies navigation in your app.
- [class NSTreeController](nstreecontroller.md)
  A bindings-compatible controller that manages a tree of objects.
- [class NSTreeNode](nstreenode.md)
  A node in a tree of nodes.
### Array-Based Data
- [class NSArrayController](nsarraycontroller.md)
  A bindings-compatible controller that manages a collection of objects.
### Key-Value Data
- [class NSDictionaryController](nsdictionarycontroller.md)
  A bindings-compatible controller that manages the display and editing of a dictionary of key-value pairs.
- [class NSDictionaryControllerKeyValuePair](nsdictionarycontrollerkeyvaluepair.md)
  A set of methods implemented by arranged objects to give access to information about those objects.
- [struct NSBindingName](nsbindingname.md)
  Values that specify a binding for certain methods.
- [struct NSBindingOption](nsbindingoption.md)
- [struct NSBindingInfoKey](nsbindinginfokey.md)
- [func NSIsControllerMarker(Any?) -> Bool](nsiscontrollermarker(_:).md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
- [NSKeyValueBindingCreation](../ObjectiveC/nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [Binding dictionary keys](binding-dictionary-keys.md)
  These constants define keys in the binding information dictionary.
### Data Placeholders
- [class NSBindingSelectionMarker](nsbindingselectionmarker.md)
- [NSPlaceholders](nsplaceholders.md)
  A set of methods that an object can implement to register default placeholders to be displayed for a binding, when no other placeholder is specified.

## See Also

- [App and Environment](app-and-environment.md)
  Learn about the objects that you use to interact with the system.
- [Documents, Data, and Pasteboard](documents-data-and-pasteboard.md)
  Organize your app’s data and preferences, and share that data on the pasteboard or in iCloud.
- [Resource Management](resource-management.md)
  Manage the storyboards and nib files containing your app’s user interface, and learn how to load data that is stored in resource files.
- [App Extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/cocoa-bindings)*